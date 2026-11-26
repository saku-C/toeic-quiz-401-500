const SHEET_NAME = "アクセスログ";
const HEADERS = [
  "日時",
  "イベント",
  "端末ID",
  "端末通算訪問回数",
  "端末種別",
  "ブラウザ",
  "画面サイズ",
  "モード",
  "回答数",
  "正解数",
  "参照元"
];
const ALLOWED_EVENTS = ["page_view", "session_summary", "quiz_complete", "sheet_click"];

function doGet(e) {
  return ContentService
    .createTextOutput(JSON.stringify({ status: "ok", service: "wordbook-logger" }))
    .setMimeType(ContentService.MimeType.JSON);
}

function doPost(e) {
  const lock = LockService.getScriptLock();
  lock.waitLock(5000);
  try {
    if (!e || !e.postData || !e.postData.contents) {
      return jsonResponse({ status: "error", message: "empty body" });
    }

    const payload = JSON.parse(e.postData.contents);
    const eventName = String(payload.event || "");
    if (ALLOWED_EVENTS.indexOf(eventName) === -1) {
      return jsonResponse({ status: "error", message: "invalid event" });
    }

    const ss = SpreadsheetApp.getActiveSpreadsheet();
    let sheet = ss.getSheetByName(SHEET_NAME);
    if (!sheet) {
      sheet = ss.insertSheet(SHEET_NAME);
    }
    if (sheet.getLastRow() === 0) {
      sheet.appendRow(HEADERS);
    }

    const nowText = Utilities.formatDate(new Date(), "Asia/Tokyo", "yyyy-MM-dd HH:mm:ss");
    sheet.appendRow([
      nowText,
      sanitizeText(eventName, 40),
      sanitizeText(payload.deviceId || "unknown", 64),
      toNonNegativeInt(payload.visitCount),
      sanitizeText(payload.deviceType || "Other", 32),
      sanitizeText(payload.browser || "Other", 32),
      sanitizeText(payload.screen || "", 32),
      sanitizeText(payload.mode || "", 24),
      toNonNegativeInt(payload.answered),
      toNonNegativeInt(payload.correct),
      sanitizeText(payload.referrer || "direct", 200)
    ]);

    return jsonResponse({ status: "ok" });
  } catch (err) {
    return jsonResponse({ status: "error", message: String(err) });
  } finally {
    lock.releaseLock();
  }
}

function sanitizeText(value, maxLen) {
  let str = String(value == null ? "" : value).trim().slice(0, maxLen);
  if (/^[=+\-@]/.test(str)) {
    str = "'" + str;
  }
  return str;
}

function toNonNegativeInt(value) {
  const n = parseInt(value, 10);
  if (isNaN(n) || n < 0) return 0;
  return n;
}

function jsonResponse(obj) {
  return ContentService
    .createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}
