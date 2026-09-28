/**
 * LayerLens feature-matrix sheet sync.
 * Pulls features/matrix.csv from the private GitHub repo and refreshes the
 * "Data" tab of this spreadsheet, in place. The "Matrix" tab reads from Data
 * via formulas (Confidence, Priority, Label are computed live there) and the
 * "Overrides" tab holds Javier's manual Impact/Effort/Decision overrides,
 * which always win over synced values.
 *
 * Setup (one time):
 * 1. Extensions -> Apps Script, paste this file.
 * 2. Project Settings -> Script properties -> add GH_TOKEN = a fine-grained
 *    GitHub personal access token, read-only, scoped ONLY to
 *    javiervio/layerlens-agentic-research (Contents: Read).
 * 3. Run syncMatrix once from the editor to authorize, check the Data tab.
 * 4. Triggers -> Add trigger -> syncMatrix, time-driven, every hour.
 *
 * The repo CSV stays canonical (the autonomous Monday run writes it).
 * This script only reads GitHub and only writes the Data tab.
 */

const REPO = 'javiervio/layerlens-agentic-research';
const FILE_PATH = 'features/matrix.csv';
const DATA_TAB = 'Data';

function syncMatrix() {
  const token = PropertiesService.getScriptProperties().getProperty('GH_TOKEN');
  if (!token) throw new Error('GH_TOKEN script property is not set.');

  const url = 'https://api.github.com/repos/' + REPO + '/contents/' + FILE_PATH;
  const resp = UrlFetchApp.fetch(url, {
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

  const rows = Utilities.parseCsv(resp.getContentText());
  if (rows.length < 2) throw new Error('CSV parsed to fewer than 2 rows; aborting without touching the sheet.');
  const width = rows[0].length;
  for (var i = 0; i < rows.length; i++) {
    while (rows[i].length < width) rows[i].push('');
    if (rows[i].length > width) throw new Error('Row ' + (i + 1) + ' wider than header; aborting.');
  }

  const ss = SpreadsheetApp.getActiveSpreadsheet();
  var tab = ss.getSheetByName(DATA_TAB) || ss.insertSheet(DATA_TAB);
  tab.clearContents();
  tab.getRange(1, 1, rows.length, width).setValues(rows);
  tab.getRange('A1').setNote('Synced from ' + REPO + '/' + FILE_PATH + ' at ' + new Date().toISOString() + '. Do not edit this tab; use Overrides.');
}
