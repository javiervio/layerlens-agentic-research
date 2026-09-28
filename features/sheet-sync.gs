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
  var H = ['Feature ID', 'Feature', 'Area', 'Pain point', 'Persona', 'Open Q', 'Idea ID', 'Evidence links', 'Source dates', 'Maturity', 'Impact', 'Effort', 'Confidence', 'Priority', 'Label', 'Status', 'Overridden', 'Notes', 'Last update'];
  m.getRange(1, 1, 1, H.length).setValues([H]).setFontWeight('bold');
  m.setFrozenRows(1);
  m.setFrozenColumns(2);
  var pass = { A: 'A', B: 'B', C: 'C', D: 'D', E: 'E', F: 'F', G: 'G', H: 'H', I: 'I', J: 'J', P: 'P', R: 'R' };
  for (var col in pass) {
    m.getRange(col + '2').setFormula('=ARRAYFORMULA(IF(Data!A2:A="",,Data!' + pass[col] + '2:' + pass[col] + '))');
  }
  m.getRange('K2').setFormula('=ARRAYFORMULA(IF(Data!A2:A="",,IF(IFERROR(VLOOKUP(Data!A2:A,Overrides!A:C,2,0),"")<>"",IFERROR(VLOOKUP(Data!A2:A,Overrides!A:C,2,0),""),Data!K2:K)))');
  m.getRange('L2').setFormula('=ARRAYFORMULA(IF(Data!A2:A="",,IF(IFERROR(VLOOKUP(Data!A2:A,Overrides!A:C,3,0),"")<>"",IFERROR(VLOOKUP(Data!A2:A,Overrides!A:C,3,0),""),Data!L2:L)))');
  m.getRange('M2').setFormula('=ARRAYFORMULA(IF(Data!A2:A="",,LET(b,IF(Data!J2:J="L2",0.9,IF(Data!J2:J="L1",0.6,0.3))+IF(Data!P2:P="Checked",0.1,0),IF(b>1,1,b))))');
  m.getRange('N2').setFormula('=ARRAYFORMULA(IF(A2:A="",,ROUND(K2:K*M2:M/L2:L,2)))');
  m.getRange('O2').setFormula('=ARRAYFORMULA(IF(A2:A="",,LET(d,IFERROR(VLOOKUP(A2:A,Overrides!A:D,4,0),""),IF(d<>"",d,IF(J2:J="L0","Needs evidence",IF((K2:K>=4)*(L2:L<=2),"Quick win",IF((K2:K>=4)*(L2:L>=4),"Big bet",IF((K2:K<=2)*(L2:L>=4),"Reconsider","Proposed"))))))))');
  m.getRange('Q2').setFormula('=ARRAYFORMULA(IF(A2:A="",,IF((IFERROR(VLOOKUP(A2:A,Overrides!A:D,2,0),"")<>"")+(IFERROR(VLOOKUP(A2:A,Overrides!A:D,3,0),"")<>"")+(IFERROR(VLOOKUP(A2:A,Overrides!A:D,4,0),"")<>""),"yes","")))');
  m.getRange('S2').setFormula('=ARRAYFORMULA(IF(Data!A2:A="",,Data!T2:T))');
  data.hideSheet(); // Data is the machine-written mirror; keep only Matrix + Overrides visible
  ss.setActiveSheet(m);
}

function installTrigger() {
  ScriptApp.getProjectTriggers().forEach(function (t) {
    if (t.getHandlerFunction() === 'syncMatrix') ScriptApp.deleteTrigger(t);
  });
  ScriptApp.newTrigger('syncMatrix').timeBased().everyHours(1).create();
}
