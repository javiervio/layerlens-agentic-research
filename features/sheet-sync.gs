/**
 * LayerLens feature-matrix sheet: sync + one-time setup.
 * Data / ThesesData tabs = synced from GitHub (hidden, never hand-edited).
 * Matrix tab = designer-first live view (Confidence/Priority/Label computed).
 * Theses tab = live view of field theses (direction, evidence count, last change).
 * Overrides tab = Javier's Impact/Effort/Decision overrides; they always win.
 *
 * One-time: set Script property GH_TOKEN (fine-grained, read-only, this repo),
 * then run setupAll() once and authorize. Repo CSVs stay canonical.
 */

var REPO = 'javiervio/layerlens-agentic-research';
var MATRIX_CSV = 'features/matrix.csv';
var THESES_CSV = 'knowledge/theses.csv';

function setupAll() { setupSheet(); syncMatrix(); installTrigger(); }

function ghRaw(path) {
  var token = PropertiesService.getScriptProperties().getProperty('GH_TOKEN');
  if (!token) throw new Error('GH_TOKEN script property is not set.');
  var url = 'https://api.github.com/repos/' + REPO + '/contents/' + path;
  var resp = UrlFetchApp.fetch(url, {
    headers: { Authorization: 'Bearer ' + token, Accept: 'application/vnd.github.raw+json', 'X-GitHub-Api-Version': '2022-11-28' },
    muteHttpExceptions: true
  });
  if (resp.getResponseCode() !== 200) throw new Error('GitHub fetch failed for ' + path + ': HTTP ' + resp.getResponseCode());
  return resp.getContentText();
}

function padRows(csvText) {
  var rows = Utilities.parseCsv(csvText);
  if (rows.length < 2) throw new Error('CSV parsed to fewer than 2 rows; aborting.');
  var w = rows[0].length;
  for (var i = 0; i < rows.length; i++) {
    while (rows[i].length < w) rows[i].push('');
    if (rows[i].length > w) throw new Error('Row ' + (i + 1) + ' wider than header; aborting.');
  }
  return rows;
}

function writeDataTab(name, rows, srcPath) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var tab = ss.getSheetByName(name) || ss.insertSheet(name);
  tab.clearContents();
  var range = tab.getRange(1, 1, rows.length, rows[0].length);
  range.setNumberFormat('@'); // plain text so dates mirror the CSV verbatim
  range.setValues(rows);
  tab.getRange('A1').setNote('Synced from ' + REPO + '/' + srcPath + ' at ' + new Date().toISOString() + '. Do not edit; use Overrides.');
  return tab;
}

function syncMatrix() {
  writeDataTab('Data', padRows(ghRaw(MATRIX_CSV)), MATRIX_CSV);
  try { writeDataTab('ThesesData', padRows(ghRaw(THESES_CSV)), THESES_CSV); }
  catch (e) { /* theses optional; leave prior ThesesData if fetch fails */ }
}

function setupSheet() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var data = ss.getSheetByName('Data');
  if (!data) { var s1 = ss.getSheetByName('Sheet1'); data = s1 ? s1.setName('Data') : ss.insertSheet('Data'); }
  var thData = ss.getSheetByName('ThesesData') || ss.insertSheet('ThesesData');

  var ov = ss.getSheetByName('Overrides') || ss.insertSheet('Overrides');
  ov.getRange(1, 1, 1, 5).setValues([['Feature ID', 'Impact override', 'Effort override', 'Decision', 'Note']]).setFontWeight('bold');
  ov.setFrozenRows(1);

  // Reusable, layout-independent expressions (reference Data + Overrides, never Matrix self-cells).
  var IMPACT = 'IF(IFERROR(VLOOKUP(Data!A2:A,Overrides!A:C,2,0),"")<>"",IFERROR(VLOOKUP(Data!A2:A,Overrides!A:C,2,0),""),Data!K2:K)';
  var EFFORT = 'IF(IFERROR(VLOOKUP(Data!A2:A,Overrides!A:C,3,0),"")<>"",IFERROR(VLOOKUP(Data!A2:A,Overrides!A:C,3,0),""),Data!L2:L)';
  var CONF = 'LET(b,IF(Data!J2:J="L2",0.9,IF(Data!J2:J="L1",0.6,0.3))+IF(Data!P2:P="Checked",0.1,0),IF(b>1,1,b))';
  var PRIORITY = '=ARRAYFORMULA(IF(Data!A2:A="",,ROUND((' + IMPACT + ')*(' + CONF + ')/(' + EFFORT + '),2)))';
  var LABEL = '=ARRAYFORMULA(IF(Data!A2:A="",,LET(im,' + IMPACT + ',ef,' + EFFORT + ',d,IFERROR(VLOOKUP(Data!A2:A,Overrides!A:D,4,0),""),IF(d<>"",d,IF(Data!J2:J="L0","Needs evidence",IF((im>=4)*(ef<=2),"Quick win",IF((im>=4)*(ef>=4),"Big bet",IF((im<=2)*(ef>=4),"Reconsider","Proposed"))))))))';
  var OVERRIDE = '=ARRAYFORMULA(IF(Data!A2:A="",,IF((IFERROR(VLOOKUP(Data!A2:A,Overrides!A:D,2,0),"")<>"")+(IFERROR(VLOOKUP(Data!A2:A,Overrides!A:D,3,0),"")<>"")+(IFERROR(VLOOKUP(Data!A2:A,Overrides!A:D,4,0),"")<>""),"yes","")))';

  // Matrix view. 'd' = pass-through Data col; 'f' = literal formula. Idea ID (Data G) intentionally NOT in the view.
  // Data cols: A id B feature C area D pain E persona F openQ G ideaID H evid I srcDates J maturity K impact L effort
  //            M confCSV N priCSV O labelCSV P status Q diff R notes S dateAdded T lastUpdate U inPlainTerms V evid# W whatMoved
  var COLS = [
    ['Feature ID', 'd', 'A'],
    ['Feature', 'd', 'B'],
    ['In plain terms', 'd', 'U'],
    ['Priority', 'f', PRIORITY],
    ['Label', 'f', LABEL],
    ['What moved', 'd', 'W'],
    ['Evidence (#)', 'd', 'V'],
    ['Impact', 'f', '=ARRAYFORMULA(IF(Data!A2:A="",,' + IMPACT + '))'],
    ['Effort', 'f', '=ARRAYFORMULA(IF(Data!A2:A="",,' + EFFORT + '))'],
    ['Confidence', 'f', '=ARRAYFORMULA(IF(Data!A2:A="",,' + CONF + '))'],
    ['Maturity', 'd', 'J'],
    ['Area', 'd', 'C'],
    ['Pain point', 'd', 'D'],
    ['Persona', 'd', 'E'],
    ['Differentiator angle', 'd', 'Q'],
    ['Open Q', 'd', 'F'],
    ['Status', 'd', 'P'],
    ['Override applied?', 'f', OVERRIDE],
    ['Evidence links', 'd', 'H'],
    ['Source dates', 'd', 'I'],
    ['Notes', 'd', 'R'],
    ['Date added', 'd', 'S'],
    ['Last update', 'd', 'T']
  ];
  var m = ss.getSheetByName('Matrix') || ss.insertSheet('Matrix', 0);
  m.clear();
  m.clearConditionalFormatRules();
  var headers = COLS.map(function (c) { return c[0]; });
  m.getRange(1, 1, 1, headers.length).setValues([headers]).setFontWeight('bold');
  m.setFrozenRows(1);
  m.setFrozenColumns(2);
  function L(i) { var s = ''; i++; while (i > 0) { var r = (i - 1) % 26; s = String.fromCharCode(65 + r) + s; i = Math.floor((i - 1) / 26); } return s; }
  for (var i = 0; i < COLS.length; i++) {
    var f = COLS[i][1] === 'd' ? '=ARRAYFORMULA(IF(Data!A2:A="",,Data!' + COLS[i][2] + '2:' + COLS[i][2] + '))' : COLS[i][2];
    m.getRange(L(i) + '2').setFormula(f);
  }
  m.setColumnWidth(3, 360); // In plain terms
  m.setColumnWidth(6, 300); // What moved
  m.getRange('C:C').setWrap(true);
  m.getRange('F:F').setWrap(true);

  // Conditional formatting: colour the Label column (col E = index 4).
  var mRules = [];
  function rule(sheet, a1, text, bg) {
    mRules.push(SpreadsheetApp.newConditionalFormatRule().whenTextContains(text).setBackground(bg).setRanges([sheet.getRange(a1)]).build());
  }
  rule(m, 'E2:E', 'Quick win', '#d9ead3');
  rule(m, 'E2:E', 'Big bet', '#cfe2f3');
  rule(m, 'E2:E', 'Reconsider', '#f4cccc');
  rule(m, 'E2:E', 'Needs evidence', '#efefef');
  m.setConditionalFormatRules(mRules);

  // Theses view (pass-through of ThesesData A..F).
  var t = ss.getSheetByName('Theses') || ss.insertSheet('Theses', 1);
  t.clear();
  t.clearConditionalFormatRules();
  var tHeaders = ['Thesis ID', 'Statement', 'Direction', 'Evidence (#)', 'Last change', 'Stratix implication'];
  t.getRange(1, 1, 1, tHeaders.length).setValues([tHeaders]).setFontWeight('bold');
  t.setFrozenRows(1);
  for (var j = 0; j < 6; j++) {
    var cc = L(j);
    t.getRange(cc + '2').setFormula('=ARRAYFORMULA(IF(ThesesData!A2:A="",,ThesesData!' + cc + '2:' + cc + '))');
  }
  t.setColumnWidth(2, 420); // Statement
  t.setColumnWidth(6, 380); // Stratix implication
  t.getRange('B:B').setWrap(true);
  t.getRange('F:F').setWrap(true);
  var tRules = [];
  tRules.push(SpreadsheetApp.newConditionalFormatRule().whenTextContains('strengthening').setBackground('#d9ead3').setRanges([t.getRange('C2:C')]).build());
  tRules.push(SpreadsheetApp.newConditionalFormatRule().whenTextContains('weakening').setBackground('#f4cccc').setRanges([t.getRange('C2:C')]).build());
  tRules.push(SpreadsheetApp.newConditionalFormatRule().whenTextContains('broken').setBackground('#ea9999').setRanges([t.getRange('C2:C')]).build());
  tRules.push(SpreadsheetApp.newConditionalFormatRule().whenTextContains('nursery').setBackground('#efefef').setRanges([t.getRange('C2:C')]).build());
  tRules.push(SpreadsheetApp.newConditionalFormatRule().whenTextContains('stable').setBackground('#fff2cc').setRanges([t.getRange('C2:C')]).build());
  t.setConditionalFormatRules(tRules);

  data.hideSheet();
  thData.hideSheet();
  ss.setActiveSheet(m);
}

function installTrigger() {
  ScriptApp.getProjectTriggers().forEach(function (tr) { if (tr.getHandlerFunction() === 'syncMatrix') ScriptApp.deleteTrigger(tr); });
  ScriptApp.newTrigger('syncMatrix').timeBased().everyHours(1).create();
}
