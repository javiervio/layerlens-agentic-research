/**
 * LayerLens feature-matrix sheet: sync + one-time setup.
 * Data tab = synced from GitHub (never hand-edited).
 * Matrix tab = live view with formulas (Confidence from maturity, Priority, Label).
 * Overrides tab = Javier's Impact/Effort/Decision overrides; they always win.
 *
 * One-time: set Script property GH_TOKEN (fine-grained, read-only, this repo),
 * then run setupAll() once and authorize. It builds tabs, syncs, and installs
 * the hourly trigger. The repo CSV stays canonical.
 */

var REPO = 'javiervio/layerlens-agentic-research';
var FILE_PATH = 'features/matrix.csv';

function setupAll() {
  setupSheet();
  syncMatrix();
  installTrigger();
}

function syncMatrix() {
  var token = PropertiesService.getScriptProperties().getProperty('GH_TOKEN');
  if (!token) throw new Error('GH_TOKEN script property is not set.');
  var url = 'https://api.github.com/repos/' + REPO + '/contents/' + FILE_PATH;
  var resp = UrlFetchApp.fetch(url, {
    headers: {
      Authorization: 'Bearer ' + token,
      Accept: 'application/vnd.github.raw+json',
      'X-GitHub-Api-Version': '2022-11-28'
    },
    muteHttpExceptions: true
  });
  if (resp.getResponseCode() !== 200) {
    throw new Error('GitHub fetch failed: HTTP ' + resp.getResponseCode() + ' ' + resp.getContentText().slice(0, 200));
  }
  var rows = Utilities.parseCsv(resp.getContentText());
  if (rows.length < 2) throw new Error('CSV parsed to fewer than 2 rows; aborting without touching the sheet.');
  var width = rows[0].length;
  for (var i = 0; i < rows.length; i++) {
    while (rows[i].length < width) rows[i].push('');
    if (rows[i].length > width) throw new Error('Row ' + (i + 1) + ' wider than header; aborting.');
  }
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var tab = ss.getSheetByName('Data') || ss.insertSheet('Data');
  tab.clearContents();
  var range = tab.getRange(1, 1, rows.length, width);
  range.setNumberFormat('@'); // force plain text so dates mirror the CSV verbatim (no serial coercion)
  range.setValues(rows);
  tab.getRange('A1').setNote('Synced from ' + REPO + '/' + FILE_PATH + ' at ' + new Date().toISOString() + '. Do not edit this tab; use Overrides.');
}

function setupSheet() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var data = ss.getSheetByName('Data');
  if (!data) {
    var s1 = ss.getSheetByName('Sheet1');
    data = s1 ? s1.setName('Data') : ss.insertSheet('Data');
  }
  var ov = ss.getSheetByName('Overrides') || ss.insertSheet('Overrides');
  ov.getRange(1, 1, 1, 5).setValues([['Feature ID', 'Impact override', 'Effort override', 'Decision', 'Note']]).setFontWeight('bold');
  ov.setFrozenRows(1);
  var m = ss.getSheetByName('Matrix') || ss.insertSheet('Matrix', 0);
  m.clear();
  // Designer-first Matrix layout. Each entry: [header, kind, arg].
  // kind 'd' = pass-through from Data column arg; kind 'f' = literal formula arg.
  // Data cols: A FeatureID B Feature C Area D Pain E Persona F OpenQ G IdeaID
  // H Evidence I SourceDates J Maturity K Impact L Effort ... P Status Q Diff R Notes S DateAdded T LastUpdate U InPlainTerms
  var COLS = [
    ['Feature ID', 'd', 'A'],
    ['Feature', 'd', 'B'],
    ['In plain terms', 'd', 'U'],
    ['Priority', 'f', '=ARRAYFORMULA(IF(A2:A="",,ROUND(F2:F*H2:H/G2:G,2)))'],
    ['Label', 'f', '=ARRAYFORMULA(IF(Data!A2:A="",,LET(d,IFERROR(VLOOKUP(Data!A2:A,Overrides!A:D,4,0),""),IF(d<>"",d,IF(Data!J2:J="L0","Needs evidence",IF((F2:F>=4)*(G2:G<=2),"Quick win",IF((F2:F>=4)*(G2:G>=4),"Big bet",IF((F2:F<=2)*(G2:G>=4),"Reconsider","Proposed"))))))))'],
    ['Impact', 'f', '=ARRAYFORMULA(IF(Data!A2:A="",,IF(IFERROR(VLOOKUP(Data!A2:A,Overrides!A:C,2,0),"")<>"",IFERROR(VLOOKUP(Data!A2:A,Overrides!A:C,2,0),""),Data!K2:K)))'],
    ['Effort', 'f', '=ARRAYFORMULA(IF(Data!A2:A="",,IF(IFERROR(VLOOKUP(Data!A2:A,Overrides!A:C,3,0),"")<>"",IFERROR(VLOOKUP(Data!A2:A,Overrides!A:C,3,0),""),Data!L2:L)))'],
    ['Confidence', 'f', '=ARRAYFORMULA(IF(Data!A2:A="",,LET(b,IF(Data!J2:J="L2",0.9,IF(Data!J2:J="L1",0.6,0.3))+IF(Data!P2:P="Checked",0.1,0),IF(b>1,1,b))))'],
    ['Maturity', 'd', 'J'],
    ['Area', 'd', 'C'],
    ['Pain point', 'd', 'D'],
    ['Persona', 'd', 'E'],
    ['Differentiator angle', 'd', 'Q'],
    ['Open Q', 'd', 'F'],
    ['Status', 'd', 'P'],
    ['Override applied?', 'f', '=ARRAYFORMULA(IF(Data!A2:A="",,IF((IFERROR(VLOOKUP(Data!A2:A,Overrides!A:D,2,0),"")<>"")+(IFERROR(VLOOKUP(Data!A2:A,Overrides!A:D,3,0),"")<>"")+(IFERROR(VLOOKUP(Data!A2:A,Overrides!A:D,4,0),"")<>""),"yes","")))'],
    ['Idea ID', 'd', 'G'],
    ['Evidence links', 'd', 'H'],
    ['Source dates', 'd', 'I'],
    ['Notes', 'd', 'R'],
    ['Date added', 'd', 'S'],
    ['Last update', 'd', 'T']
  ];
  var headers = COLS.map(function (c) { return c[0]; });
  m.getRange(1, 1, 1, headers.length).setValues([headers]).setFontWeight('bold');
  m.setFrozenRows(1);
  m.setFrozenColumns(2);
  function colLetter(i) { var s = ''; i++; while (i > 0) { var r = (i - 1) % 26; s = String.fromCharCode(65 + r) + s; i = Math.floor((i - 1) / 26); } return s; }
  for (var i = 0; i < COLS.length; i++) {
    var f = COLS[i][1] === 'd'
      ? '=ARRAYFORMULA(IF(Data!A2:A="",,Data!' + COLS[i][2] + '2:' + COLS[i][2] + '))'
      : COLS[i][2];
    m.getRange(colLetter(i) + '2').setFormula(f);
  }
  m.setColumnWidth(3, 380);      // widen "In plain terms"
  m.getRange('C:C').setWrap(true);
  data.hideSheet(); // Data is the machine-written mirror; keep only Matrix + Overrides visible
  ss.setActiveSheet(m);
}

function installTrigger() {
  ScriptApp.getProjectTriggers().forEach(function (t) {
    if (t.getHandlerFunction() === 'syncMatrix') ScriptApp.deleteTrigger(t);
  });
  ScriptApp.newTrigger('syncMatrix').timeBased().everyHours(1).create();
}
