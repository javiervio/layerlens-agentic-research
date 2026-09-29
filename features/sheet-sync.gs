/**
 * LayerLens feature matrix, human-first sheet.
 *
 * Tabs the reader sees:
 *   - "Next up": features ranked best-first. Feature, plain description, Impact,
 *     Effort, a recommendation in words, why now, and a one-click link to evidence.
 *   - "Evidence": readable, one row per source, real titles + clickable links +
 *     what it said + how it moved the feature.
 *   - "Theses": the field hypotheses and their direction (validated / weakening).
 *   - "Overrides": Javier's Impact/Effort/Decision overrides; they always win.
 * Hidden raw mirrors: Data, EvidenceData, ThesesData (synced from the repo CSVs).
 *
 * One-time: set Script property GH_TOKEN (fine-grained, read-only, this repo),
 * run setupAll() once, authorize. Then it refreshes hourly. Repo CSVs are canonical.
 * Menu "LayerLens > Refresh now" forces a rebuild (e.g. after editing Overrides).
 */

var REPO = 'javiervio/layerlens-agentic-research';
var MATRIX_CSV = 'features/matrix.csv';
var EVIDENCE_CSV = 'features/evidence.csv';
var THESES_CSV = 'knowledge/theses.csv';

var IMPACT_WORD = { 5: 'Very high', 4: 'High', 3: 'Medium', 2: 'Low', 1: 'Minimal' };
var EFFORT_WORD = { 1: 'Very low', 2: 'Low', 3: 'Medium', 4: 'High', 5: 'Very high' };

function setupAll() { buildAll(); installTrigger(); }
function onOpen() { SpreadsheetApp.getUi().createMenu('LayerLens').addItem('Refresh now', 'buildAll').addToUi(); }

function ghRaw(path) {
  var token = PropertiesService.getScriptProperties().getProperty('GH_TOKEN');
  if (!token) throw new Error('GH_TOKEN script property is not set.');
  var resp = UrlFetchApp.fetch('https://api.github.com/repos/' + REPO + '/contents/' + path, {
    headers: { Authorization: 'Bearer ' + token, Accept: 'application/vnd.github.raw+json', 'X-GitHub-Api-Version': '2022-11-28' },
    muteHttpExceptions: true
  });
  if (resp.getResponseCode() !== 200) throw new Error('GitHub fetch failed for ' + path + ': HTTP ' + resp.getResponseCode());
  return resp.getContentText();
}

function pad(csvText) {
  var rows = Utilities.parseCsv(csvText);
  if (rows.length < 2) throw new Error('CSV too short: ' + csvText.slice(0, 80));
  var w = rows[0].length;
  for (var i = 0; i < rows.length; i++) { while (rows[i].length < w) rows[i].push(''); }
  return rows;
}
function idx(header) { var m = {}; for (var i = 0; i < header.length; i++) m[header[i]] = i; return m; }
function writeHidden(name, rows) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var t = ss.getSheetByName(name) || ss.insertSheet(name);
  t.clearContents();
  t.getRange(1, 1, rows.length, rows[0].length).setNumberFormat('@').setValues(rows);
  return t;
}

function buildAll() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var matrix = pad(ghRaw(MATRIX_CSV));
  var evidence = null, theses = null;
  try { evidence = pad(ghRaw(EVIDENCE_CSV)); } catch (e) {}
  try { theses = pad(ghRaw(THESES_CSV)); } catch (e) {}

  writeHidden('Data', matrix);
  if (evidence) writeHidden('EvidenceData', evidence);
  if (theses) writeHidden('ThesesData', theses);

  var ov = ensureOverrides();
  var overrides = readOverrides(ov);

  var evTab = buildEvidence(evidence, matrix);   // build first so Next up can link to its gid
  buildNextUp(matrix, overrides, evTab.getSheetId());
  buildTheses(theses);

  ['Data', 'EvidenceData', 'ThesesData'].forEach(function (n) { var s = ss.getSheetByName(n); if (s) s.hideSheet(); });
  var old = ss.getSheetByName('Matrix'); if (old) ss.deleteSheet(old); // remove the old dense tab
  ss.setActiveSheet(ss.getSheetByName('Next up'));
}

function ensureOverrides() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var ov = ss.getSheetByName('Overrides') || ss.insertSheet('Overrides');
  if (ov.getRange('A1').getValue() !== 'Feature ID') {
    ov.getRange(1, 1, 1, 5).setValues([['Feature ID', 'Impact override', 'Effort override', 'Decision', 'Note']]).setFontWeight('bold');
    ov.setFrozenRows(1);
  }
  return ov;
}
function readOverrides(ov) {
  var map = {}, last = ov.getLastRow();
  if (last < 2) return map;
  var vals = ov.getRange(2, 1, last - 1, 4).getValues();
  vals.forEach(function (r) { if (r[0]) map[String(r[0]).trim()] = { impact: r[1], effort: r[2], decision: r[3] }; });
  return map;
}

function num(v) { var n = parseFloat(v); return isNaN(n) ? '' : n; }

function buildNextUp(matrix, overrides, evGid) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var h = idx(matrix[0]);
  var items = [];
  for (var i = 1; i < matrix.length; i++) {
    var r = matrix[i];
    if (!r[h['Feature ID']]) continue;
    var id = r[h['Feature ID']];
    var o = overrides[id] || {};
    var impact = num(o.impact !== undefined && o.impact !== '' ? o.impact : r[h['Impact (1-5)']]);
    var effort = num(o.effort !== undefined && o.effort !== '' ? o.effort : r[h['Effort (1-5)']]);
    var maturity = r[h['Maturity']];
    var checked = r[h['Status']] === 'Checked';
    var conf = maturity === 'L2' ? 0.9 : (maturity === 'L1' ? 0.6 : 0.3); if (checked) conf = Math.min(1, conf + 0.1);
    var priority = (impact && effort) ? Math.round(impact * conf / effort * 100) / 100 : 0;
    var decision = o.decision;
    var rec;
    if (decision) rec = decision;
    else if (maturity === 'L0') rec = 'Gather evidence first';
    else if (impact >= 4 && effort <= 2) rec = 'Build next (quick win)';
    else if (impact >= 4 && effort >= 4) rec = 'Plan a slot (big bet)';
    else if (impact <= 2 && effort >= 4) rec = 'Reconsider';
    else rec = 'Strong candidate';
    items.push({
      id: id, feature: r[h['Feature']], plain: r[h['In plain terms']],
      impact: impact, effort: effort, priority: priority, rec: rec,
      why: r[h['Why now']] || '', evCount: num(r[h['Evidence (#)']]) || 0, maturity: maturity
    });
  }
  items.sort(function (a, b) { return b.priority - a.priority; });

  var headers = ['#', 'Feature', 'What it does', 'Impact', 'Effort', 'Recommendation', 'Why now', 'Evidence', 'ref'];
  var t = ss.getSheetByName('Next up') || ss.insertSheet('Next up', 0);
  t.clear(); t.clearConditionalFormatRules();
  t.getRange(1, 1, 1, headers.length).setValues([headers]).setFontWeight('bold');
  var rowsOut = [], evFormulas = [];
  for (var k = 0; k < items.length; k++) {
    var it = items[k];
    rowsOut.push([
      k + 1, it.feature, it.plain,
      it.impact ? (IMPACT_WORD[it.impact] + ' (' + it.impact + ')') : '',
      it.effort ? (EFFORT_WORD[it.effort] + ' (' + it.effort + ')') : '',
      it.rec, it.why, '', it.id
    ]);
    evFormulas.push('=HYPERLINK("#gid=' + evGid + '","See ' + it.evCount + ' source' + (it.evCount === 1 ? '' : 's') + ' →")');
  }
  if (rowsOut.length) {
    t.getRange(2, 1, rowsOut.length, headers.length).setValues(rowsOut);
    for (var m2 = 0; m2 < evFormulas.length; m2++) t.getRange(2 + m2, 8).setFormula(evFormulas[m2]);
  }
  t.setFrozenRows(1);
  t.setColumnWidth(1, 34);   // #
  t.setColumnWidth(2, 230);  // Feature
  t.setColumnWidth(3, 430);  // What it does
  t.setColumnWidth(4, 90); t.setColumnWidth(5, 90);
  t.setColumnWidth(6, 150);  // Recommendation
  t.setColumnWidth(7, 430);  // Why now
  t.setColumnWidth(8, 130);  // Evidence
  t.setColumnWidth(9, 60);   // ref
  t.getRange('C:C').setWrap(true); t.getRange('G:G').setWrap(true);
  t.getRange(1, 9, t.getMaxRows(), 1).setFontColor('#b7b7b7'); // ref column muted

  var rules = [];
  function rule(a1, text, bg) { rules.push(SpreadsheetApp.newConditionalFormatRule().whenTextContains(text).setBackground(bg).setRanges([t.getRange(a1)]).build()); }
  rule('F2:F', 'Build next', '#b6d7a8');
  rule('F2:F', 'Strong candidate', '#d9ead3');
  rule('F2:F', 'big bet', '#cfe2f3');
  rule('F2:F', 'Gather evidence', '#efefef');
  rule('F2:F', 'Reconsider', '#f4cccc');
  t.setConditionalFormatRules(rules);
}

function buildEvidence(evidence, matrix) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var t = ss.getSheetByName('Evidence') || ss.insertSheet('Evidence', 1);
  t.clear();
  var headers = ['Feature', 'Source', 'What it says', 'How it moved this feature', 'Link'];
  t.getRange(1, 1, 1, headers.length).setValues([headers]).setFontWeight('bold');
  t.setFrozenRows(1);
  if (evidence) {
    var eh = idx(evidence[0]);
    // resolve feature id -> name
    var mh = idx(matrix[0]); var name = {};
    for (var i = 1; i < matrix.length; i++) name[matrix[i][mh['Feature ID']]] = matrix[i][mh['Feature']];
    var out = [], links = [];
    for (var j = 1; j < evidence.length; j++) {
      var r = evidence[j]; if (!r[eh['Feature ID']]) continue;
      out.push([name[r[eh['Feature ID']]] || r[eh['Feature ID']], r[eh['Source']], r[eh['What it says']], r[eh['How it moved this feature']], '']);
      var lk = r[eh['Link']];
      links.push((lk && lk !== 'internal') ? '=HYPERLINK("' + lk + '","open")' : 'internal');
    }
    if (out.length) {
      t.getRange(2, 1, out.length, headers.length).setValues(out);
      for (var k = 0; k < links.length; k++) { if (links[k].charAt(0) === '=') t.getRange(2 + k, 5).setFormula(links[k]); else t.getRange(2 + k, 5).setValue(links[k]); }
    }
  }
  t.setColumnWidth(1, 250); t.setColumnWidth(2, 300); t.setColumnWidth(3, 380); t.setColumnWidth(4, 380); t.setColumnWidth(5, 70);
  t.getRange('A:D').setWrap(true);
  return t;
}

function buildTheses(theses) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var t = ss.getSheetByName('Theses') || ss.insertSheet('Theses', 2);
  t.clear(); t.clearConditionalFormatRules();
  var headers = ['What we believe', 'Direction', 'How strong (sources)', 'Latest change', 'What it means for Stratix'];
  t.getRange(1, 1, 1, headers.length).setValues([headers]).setFontWeight('bold');
  t.setFrozenRows(1);
  if (theses) {
    var th = idx(theses[0]); var out = [];
    for (var i = 1; i < theses.length; i++) {
      var r = theses[i]; if (!r[th['Statement']]) continue;
      out.push([r[th['Statement']], r[th['Direction']], r[th['Evidence (#)']], r[th['Last change']], r[th['Stratix implication']]]);
    }
    if (out.length) t.getRange(2, 1, out.length, headers.length).setValues(out);
  }
  t.setColumnWidth(1, 430); t.setColumnWidth(2, 110); t.setColumnWidth(3, 130); t.setColumnWidth(4, 300); t.setColumnWidth(5, 380);
  t.getRange('A:A').setWrap(true); t.getRange('D:E').setWrap(true);
  var rules = [];
  function r2(text, bg) { rules.push(SpreadsheetApp.newConditionalFormatRule().whenTextContains(text).setBackground(bg).setRanges([t.getRange('B2:B')]).build()); }
  r2('strengthening', '#b6d7a8'); r2('weakening', '#f4cccc'); r2('broken', '#ea9999'); r2('nursery', '#efefef'); r2('stable', '#fff2cc');
  t.setConditionalFormatRules(rules);
}

function installTrigger() {
  ScriptApp.getProjectTriggers().forEach(function (tr) { var f = tr.getHandlerFunction(); if (f === 'buildAll' || f === 'syncMatrix') ScriptApp.deleteTrigger(tr); });
  ScriptApp.newTrigger('buildAll').timeBased().everyHours(1).create();
}
