# -*- coding: utf-8 -*-
"""
Web公開用 index.html 生成スクリプト
- 出題順: No.501 〜 No.600 (番号順で固定)
- 10択の選択肢: 毎回出題時/リセット時に完全にランダム生成
- 選択肢記号: 1〜0
- スクロール不要の1画面完結レイアウト (100dvh)
- 単語帳一覧モード（検索・発音・全項目表示）
- Web Speech API ネイティブ発音再生
- 問題一覧ジャンプモーダル
- Googleスプレッドシート用CSV & Excel ダウンロード
- 絵文字なし / 効果音なし
"""

import os
import shutil
import json
from quiz_data import words_data

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

all_words_json = json.dumps(words_data, ensure_ascii=False)

html_content = f'''<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>単語帳 100問10択クイズ (No.501-600)</title>
  <meta name="description" content="単語帳 No.501〜600。出題は番号順。単語帳閲覧機能、ネイティブ音声・解説付き。">
  <meta name="theme-color" content="#1e3a8a">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Noto+Sans+JP:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --primary: #2563eb;
      --primary-dark: #1d4ed8;
      --primary-light: #eff6ff;
      --success: #16a34a;
      --success-light: #dcfce7;
      --danger: #dc2626;
      --danger-light: #fee2e2;
      --bg: #f1f5f9;
      --card-bg: #ffffff;
      --text-main: #0f172a;
      --text-muted: #64748b;
      --border: #e2e8f0;
      --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
      --shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
      --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: 'Plus Jakarta Sans', 'Noto Sans JP', sans-serif;
      -webkit-tap-highlight-color: transparent;
    }}

    html, body {{
      height: 100%;
    }}

    body {{
      background: var(--bg);
      color: var(--text-main);
      height: 100dvh;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }}

    @media (max-height: 520px) {{
      body {{
        height: auto;
        min-height: 100dvh;
        overflow-y: auto;
      }}
    }}

    .container {{
      max-width: 920px;
      width: 100%;
      height: 100%;
      margin: 0 auto;
      padding: 0.5rem 0.75rem;
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
      min-height: 0;
    }}

    header {{
      flex-shrink: 0;
      background: var(--card-bg);
      padding: 0.45rem 0.85rem;
      border-radius: 0.75rem;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 0.5rem;
      border: 1px solid var(--border);
    }}

    .title-group h1 {{
      font-size: 1rem;
      font-weight: 800;
      color: #1e3a8a;
      display: flex;
      align-items: baseline;
      gap: 0.25rem;
      letter-spacing: -0.01em;
    }}

    .range-sub {{
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--text-muted);
      margin-left: 0.25rem;
    }}

    .controls {{
      display: flex;
      gap: 0.4rem;
      flex-wrap: wrap;
      align-items: center;
    }}

    select, button.control-btn, a.control-btn {{
      padding: 0.32rem 0.65rem;
      border-radius: 0.5rem;
      border: 1px solid var(--border);
      background: var(--card-bg);
      color: var(--text-main);
      font-size: 0.78rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s ease;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 0.25rem;
      user-select: none;
    }}

    select:focus, button.control-btn:focus {{
      outline: 2px solid var(--primary);
    }}

    button.control-btn:hover, a.control-btn:hover {{
      background: var(--primary-light);
      border-color: var(--primary);
      color: var(--primary-dark);
    }}

    .btn-tab-active {{
      background: #1e3a8a !important;
      color: #ffffff !important;
      border-color: #1e3a8a !important;
    }}

    /* クイズエリア */
    #quizArea {{
      flex: 1;
      min-height: 0;
      display: flex;
      flex-direction: column;
    }}

    .quiz-card {{
      flex: 1;
      min-height: 0;
      background: var(--card-bg);
      border-radius: 0.9rem;
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }}

    .progress-bar-bg {{
      height: 4px;
      width: 100%;
      background: var(--border);
      flex-shrink: 0;
    }}

    .progress-bar-fill {{
      height: 100%;
      background: linear-gradient(90deg, #2563eb, #3b82f6);
      width: 1%;
      transition: width 0.25s ease;
    }}

    .quiz-body {{
      flex: 1;
      min-height: 0;
      padding: 0.7rem 1rem 0.8rem 1rem;
      display: flex;
      flex-direction: column;
      gap: 0.55rem;
    }}

    .question-header {{
      flex-shrink: 0;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 0.4rem;
      flex-wrap: wrap;
    }}

    .header-left, .header-right {{
      display: flex;
      align-items: center;
      gap: 0.35rem;
      flex-wrap: wrap;
    }}

    .q-number {{
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--primary);
      background: var(--primary-light);
      padding: 0.24rem 0.6rem;
      border-radius: 0.45rem;
      cursor: pointer;
      transition: background 0.15s;
    }}
    .q-number:hover {{
      background: #dbeafe;
    }}

    .pos-tag {{
      font-size: 0.75rem;
      font-weight: 700;
      color: #475569;
      background: #f1f5f9;
      padding: 0.24rem 0.55rem;
      border-radius: 0.45rem;
    }}

    .mode-select {{
      padding: 0.22rem 0.45rem;
      font-size: 0.75rem;
    }}

    .stat-badge {{
      display: inline-flex;
      align-items: center;
      gap: 0.25rem;
      padding: 0.18rem 0.5rem;
      border-radius: 9999px;
      font-size: 0.75rem;
      font-weight: 700;
    }}

    .badge-correct {{ background: var(--success-light); color: var(--success); }}
    .badge-wrong {{ background: var(--danger-light); color: var(--danger); }}
    .badge-accuracy {{ background: var(--primary-light); color: var(--primary); }}

    .target-wrapper {{
      flex-shrink: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.65rem;
      padding: 0.15rem 0;
    }}

    .target-word {{
      font-size: clamp(1.35rem, 3vw, 1.95rem);
      font-weight: 800;
      color: var(--text-main);
      letter-spacing: -0.02em;
      text-align: center;
      line-height: 1.2;
    }}

    .btn-audio {{
      background: #f1f5f9;
      border: 1px solid var(--border);
      border-radius: 0.45rem;
      padding: 0.3rem 0.55rem;
      font-size: 0.75rem;
      font-weight: 700;
      color: #334155;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.2rem;
      transition: all 0.15s ease;
      flex-shrink: 0;
    }}
    .btn-audio:hover {{
      background: #e2e8f0;
      color: #0f172a;
    }}

    /* 常時2列 10択グリッド */
    .choices-grid {{
      flex-shrink: 0;
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 0.45rem 0.6rem;
    }}

    .choice-btn {{
      min-height: 40px;
      background: var(--card-bg);
      border: 1.5px solid var(--border);
      border-radius: 0.6rem;
      padding: 0.45rem 0.7rem;
      text-align: left;
      font-size: 0.9rem;
      font-weight: 500;
      color: var(--text-main);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.55rem;
      min-width: 0;
      transition: all 0.12s ease;
    }}

    .choice-btn:hover:not(:disabled) {{
      border-color: var(--primary);
      background: var(--primary-light);
    }}

    .choice-key {{
      display: flex;
      align-items: center;
      justify-content: center;
      width: 24px;
      height: 24px;
      border-radius: 5px;
      background: #f1f5f9;
      font-size: 0.75rem;
      font-weight: 700;
      color: #475569;
      flex-shrink: 0;
      border: 1px solid #cbd5e1;
    }}

    .choice-text {{
      overflow-wrap: anywhere;
      line-height: 1.25;
    }}

    .choice-btn:hover:not(:disabled) .choice-key {{
      background: var(--primary);
      color: #ffffff;
      border-color: var(--primary);
    }}

    .choice-btn.dimmed {{
      opacity: 0.5;
    }}

    .choice-btn.correct {{
      background: var(--success-light) !important;
      border-color: var(--success) !important;
      color: var(--success) !important;
      font-weight: 700;
      opacity: 1 !important;
    }}
    .choice-btn.correct .choice-key {{
      background: var(--success);
      color: #ffffff;
      border-color: var(--success);
    }}

    .choice-btn.wrong {{
      background: var(--danger-light) !important;
      border-color: var(--danger) !important;
      color: var(--danger) !important;
      font-weight: 700;
      opacity: 1 !important;
    }}
    .choice-btn.wrong .choice-key {{
      background: var(--danger);
      color: #ffffff;
      border-color: var(--danger);
    }}

    .choice-btn:disabled {{
      cursor: default;
    }}

    /* 固定位置フィードバックパネル (レイアウトシフトなし) */
    .feedback-panel {{
      flex: 1;
      min-height: 118px;
      border-radius: 0.75rem;
      border: 1px solid var(--border);
      background: #f8fafc;
      padding: 0.6rem 0.85rem;
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
      overflow: hidden;
    }}

    .feedback-panel.is-correct {{
      background: #f0fdf4;
      border-color: #86efac;
    }}

    .feedback-panel.is-wrong {{
      background: #fef2f2;
      border-color: #fca5a5;
    }}

    .feedback-idle {{
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.82rem;
      color: var(--text-muted);
      text-align: center;
    }}

    .feedback-answered {{
      display: none;
      flex: 1;
      min-height: 0;
      flex-direction: column;
      gap: 0.35rem;
    }}

    .feedback-header {{
      flex-shrink: 0;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 0.5rem;
    }}

    .result-status {{
      font-size: 0.88rem;
      font-weight: 800;
      line-height: 1.3;
    }}
    .result-status.correct {{
      color: var(--success);
    }}
    .result-status.wrong {{
      color: var(--danger);
    }}

    .btn-next {{
      background: var(--primary);
      color: #ffffff;
      border: none;
      padding: 0.45rem 1rem;
      font-size: 0.84rem;
      font-weight: 700;
      border-radius: 0.55rem;
      cursor: pointer;
      transition: background 0.15s;
      flex-shrink: 0;
      white-space: nowrap;
    }}
    .btn-next:hover {{
      background: var(--primary-dark);
    }}

    .explanation-body {{
      flex: 1;
      min-height: 0;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 0.2rem;
    }}

    .example-en-row {{
      display: flex;
      align-items: center;
      gap: 0.45rem;
      flex-wrap: wrap;
    }}

    .example-en {{
      font-size: 0.9rem;
      font-weight: 600;
      color: #1e293b;
      line-height: 1.35;
    }}

    .btn-audio-sm {{
      background: rgba(255, 255, 255, 0.8);
      border: 1px solid var(--border);
      cursor: pointer;
      font-size: 0.72rem;
      padding: 0.12rem 0.4rem;
      border-radius: 4px;
      color: var(--primary);
      font-weight: 700;
      flex-shrink: 0;
    }}
    .btn-audio-sm:hover {{
      background: #e2e8f0;
    }}

    .example-ja {{
      font-size: 0.82rem;
      color: #475569;
      line-height: 1.35;
    }}

    .notes-text {{
      font-size: 0.76rem;
      color: #64748b;
      background: rgba(255, 255, 255, 0.75);
      padding: 0.28rem 0.5rem;
      border-radius: 0.4rem;
      border: 1px dashed var(--border);
      line-height: 1.35;
    }}

    /* リザルト画面 */
    .result-view {{
      flex: 1;
      min-height: 0;
      display: none;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      padding: 1.5rem;
    }}

    .result-score {{
      font-size: 3.5rem;
      font-weight: 800;
      color: var(--primary);
      margin: 0.75rem 0;
    }}

    .result-actions {{
      display: flex;
      justify-content: center;
      gap: 0.75rem;
      margin-top: 1.5rem;
      flex-wrap: wrap;
    }}

    /* 単語帳一覧ビュー */
    .wordbook-view {{
      flex: 1;
      min-height: 0;
      display: none;
      flex-direction: column;
    }}

    .wordbook-card {{
      flex: 1;
      min-height: 0;
      display: flex;
      flex-direction: column;
      background: #ffffff;
      padding: 0.9rem 1rem;
      border-radius: 0.9rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow-sm);
    }}

    .wordbook-top {{
      flex-shrink: 0;
    }}

    .search-box {{
      width: 100%;
      padding: 0.6rem 0.85rem;
      border-radius: 0.65rem;
      border: 1px solid var(--border);
      font-size: 0.9rem;
      margin-bottom: 0.65rem;
      outline: none;
    }}
    .search-box:focus {{
      border-color: var(--primary);
    }}

    #wordListContainer {{
      flex: 1;
      min-height: 0;
      overflow-y: auto;
      padding-right: 0.2rem;
    }}

    .word-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 0.65rem;
      padding: 0.8rem 0.9rem;
      margin-bottom: 0.55rem;
    }}
    .word-card:hover {{
      box-shadow: var(--shadow-sm);
    }}
    .word-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.3rem;
      gap: 0.5rem;
    }}

    /* モーダル */
    .modal-overlay {{
      position: fixed;
      inset: 0;
      background: rgba(15, 23, 42, 0.6);
      display: none;
      align-items: center;
      justify-content: center;
      z-index: 1000;
      padding: 1rem;
    }}
    .modal-content {{
      background: #ffffff;
      border-radius: 1rem;
      max-width: 620px;
      width: 100%;
      max-height: 80vh;
      overflow-y: auto;
      padding: 1.25rem;
      box-shadow: var(--shadow-lg);
    }}
    .modal-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(48px, 1fr));
      gap: 0.45rem;
      margin-top: 0.85rem;
    }}
    .grid-num-btn {{
      height: 38px;
      border-radius: 6px;
      border: 1px solid var(--border);
      background: #f8fafc;
      font-weight: 700;
      cursor: pointer;
      font-size: 0.85rem;
      transition: all 0.15s;
    }}
    .grid-num-btn:hover {{
      border-color: var(--primary);
      background: var(--primary-light);
    }}
    .grid-num-btn.answered-correct {{ background: var(--success-light); color: var(--success); border-color: var(--success); }}
    .grid-num-btn.answered-wrong {{ background: var(--danger-light); color: var(--danger); border-color: var(--danger); }}
    .grid-num-btn.current {{ outline: 2px solid var(--primary); border-color: var(--primary); }}

    @media (max-width: 640px) {{
      .container {{
        padding: 0.35rem 0.45rem;
        gap: 0.35rem;
      }}
      header {{
        padding: 0.38rem 0.6rem;
        gap: 0.35rem;
      }}
      .title-group h1 {{
        font-size: 0.9rem;
      }}
      .range-sub {{
        font-size: 0.72rem;
      }}
      select, button.control-btn, a.control-btn {{
        padding: 0.26rem 0.48rem;
        font-size: 0.72rem;
      }}
      .quiz-body {{
        padding: 0.5rem 0.65rem 0.6rem 0.65rem;
        gap: 0.4rem;
      }}
      .choices-grid {{
        gap: 0.35rem 0.4rem;
      }}
      .choice-btn {{
        min-height: 36px;
        padding: 0.35rem 0.45rem;
        font-size: 0.78rem;
        gap: 0.35rem;
      }}
      .choice-key {{
        width: 20px;
        height: 20px;
        font-size: 0.7rem;
      }}
      .feedback-panel {{
        min-height: 105px;
        padding: 0.5rem 0.65rem;
      }}
      .btn-next {{
        padding: 0.4rem 0.75rem;
        font-size: 0.78rem;
      }}
    }}
  </style>
</head>
<body>

  <div class="container">
    <header>
      <div class="title-group">
        <h1>単語帳<span class="range-sub">No.501-600</span></h1>
      </div>
      <div class="controls">
        <button class="control-btn btn-tab-active" id="btnQuizTab" onclick="showQuizTab()">クイズ</button>
        <button class="control-btn" id="btnWordbookTab" onclick="showWordbookTab()">単語帳一覧</button>
        <button class="control-btn" onclick="openJumpModal()">進捗一覧</button>
        <a class="control-btn" href="https://docs.google.com/spreadsheets/d/1BaAIXt7jKJIoEdopA-uozzmqyQw_e2ePdSPwFk4MSac/edit?usp=sharing" target="_blank" rel="noopener">単語帳(スプレットシート)</a>
      </div>
    </header>

    <!-- クイズ画面エリア -->
    <div id="quizArea">
      <div class="quiz-card" id="quizCard">
        <div class="progress-bar-bg">
          <div class="progress-bar-fill" id="progressBar"></div>
        </div>
        <div class="quiz-body">
          <div class="question-header">
            <div class="header-left">
              <span class="q-number" id="qNumberBadge" onclick="openJumpModal()" title="クリックして問題一覧を開く">Q1 / 100 [No. 501]</span>
              <select id="modeSelect" class="mode-select" onchange="changeMode()">
                <option value="en_ja">英 → 日</option>
                <option value="ja_en">日 → 英</option>
              </select>
              <span class="pos-tag" id="posTag">動詞</span>
            </div>
            <div class="header-right">
              <span class="stat-badge badge-correct">○ <span id="correctCount">0</span></span>
              <span class="stat-badge badge-wrong">× <span id="wrongCount">0</span></span>
              <span class="stat-badge badge-accuracy"><span id="accuracyText">0.0%</span></span>
            </div>
          </div>

          <div class="target-wrapper">
            <div class="target-word" id="targetWord">aim</div>
            <button class="btn-audio" id="btnSpeakWord" title="単語の発音を聞く" onclick="speakTargetWord()">発音</button>
          </div>

          <div class="choices-grid" id="choicesGrid"></div>

          <div class="feedback-panel" id="feedbackPanel">
            <div class="feedback-idle" id="feedbackIdle">
              数字キー (1〜0) または選択肢をクリックして回答
            </div>
            <div class="feedback-answered" id="feedbackAnswered">
              <div class="feedback-header">
                <div id="resultStatus" class="result-status"></div>
                <button class="btn-next" id="btnNext" onclick="nextQuestion()">次の問題へ (Enter)</button>
              </div>
              <div class="explanation-body">
                <div class="example-en-row">
                  <span class="example-en" id="expEn"></span>
                  <button class="btn-audio-sm" id="btnSpeakSentence" title="例文の発音を聞く" onclick="speakSentence()">例文音声</button>
                </div>
                <div class="example-ja" id="expJa"></div>
                <div class="notes-text" id="expNotes"></div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="quiz-card result-view" id="resultView">
        <h2>お疲れ様でした！クイズ終了</h2>
        <p style="color: var(--text-muted); margin-top: 0.5rem;">全100問の挑戦が完了しました。</p>
        <div class="result-score" id="finalScore">95 / 100</div>
        <p id="finalAccuracy" style="font-size: 1.15rem; font-weight: 600; color: #334155;">正答率: 95.0%</p>
        <div class="result-actions">
          <button class="btn-next" style="padding: 0.7rem 1.4rem; font-size: 0.95rem;" onclick="retryWrongOnly()" id="btnRetryWrong">間違えた問題のみ復習</button>
          <button class="control-btn" style="padding: 0.7rem 1.4rem; font-size: 0.95rem;" onclick="resetQuiz()">もう一度最初から</button>
        </div>
      </div>
    </div>

    <!-- 素の単語帳一覧エリア -->
    <div id="wordbookArea" class="wordbook-view">
      <div class="wordbook-card">
        <div class="wordbook-top">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.6rem; flex-wrap: wrap; gap: 0.5rem;">
            <h2 style="font-size: 1.05rem; font-weight: 800; color: #1e3a8a;">単語帳一覧 (No.501 〜 600 全100語)</h2>
            <div style="display: flex; gap: 0.4rem; flex-wrap: wrap;">
              <a class="control-btn" href="https://docs.google.com/spreadsheets/d/1BaAIXt7jKJIoEdopA-uozzmqyQw_e2ePdSPwFk4MSac/edit?usp=sharing" target="_blank" rel="noopener">単語帳(スプレットシート)</a>
              <a class="control-btn" href="TOEIC_Words_501-600_List.csv" download>CSV保存</a>
              <a class="control-btn" href="TOEIC_Words_501-600_100Quiz.xlsx" download>Excel保存</a>
            </div>
          </div>
          <input type="text" id="searchInput" class="search-box" placeholder="単語・意味・例文を検索..." oninput="filterWordList()">
        </div>
        <div id="wordListContainer"></div>
      </div>
    </div>
  </div>

  <!-- 問題一覧ジャンプモーダル -->
  <div class="modal-overlay" id="jumpModal" onclick="closeJumpModal(event)">
    <div class="modal-content" onclick="event.stopPropagation()">
      <div style="display: flex; justify-content: space-between; align-items: center;">
        <h3 style="font-size: 1.05rem; font-weight: 700;">問題一覧 (No.501 〜 600)</h3>
        <button class="control-btn" onclick="document.getElementById('jumpModal').style.display='none'">閉じる</button>
      </div>
      <p style="font-size: 0.82rem; color: var(--text-muted); margin-top: 0.3rem;">番号をクリックするとその問題に直接ジャンプします。（出題順: 番号順）</p>
      <div class="modal-grid" id="jumpGrid"></div>
    </div>
  </div>

  <script>
    const ALL_WORDS = {all_words_json};
    const CHOICE_KEYS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"];

    let currentMode = "en_ja";
    let questionsList = [];
    let currentIndex = 0;
    let correctTotal = 0;
    let wrongTotal = 0;
    let wrongQuestions = [];
    let isAnswered = false;
    let answerHistory = {{}};
    let currentChoicesData = null;

    function generateDynamicChoices(targetItem, mode) {{
      const isEnJa = (mode === "en_ja");
      const correctAnswer = isEnJa ? targetItem.meaning : targetItem.word;

      const others = ALL_WORDS.filter(w => w.no !== targetItem.no);
      const shuffledOthers = [...others].sort(() => Math.random() - 0.5);

      const dummyAnswers = [];
      for (const item of shuffledOthers) {{
        const ans = isEnJa ? item.meaning : item.word;
        if (ans !== correctAnswer && !dummyAnswers.includes(ans)) {{
          dummyAnswers.push(ans);
        }}
        if (dummyAnswers.length === 9) break;
      }}

      const choices = [correctAnswer, ...dummyAnswers];
      choices.sort(() => Math.random() - 0.5);

      const correctLetter = CHOICE_KEYS[choices.indexOf(correctAnswer)];

      return {{
        choices: choices,
        correctLetter: correctLetter
      }};
    }}

    function init() {{
      questionsList = [...ALL_WORDS];
      currentIndex = 0;
      correctTotal = 0;
      wrongTotal = 0;
      wrongQuestions = [];
      isAnswered = false;
      answerHistory = {{}};

      document.getElementById("correctCount").textContent = "0";
      document.getElementById("wrongCount").textContent = "0";
      document.getElementById("accuracyText").textContent = "0.0%";

      document.getElementById("quizCard").style.display = "flex";
      document.getElementById("resultView").style.display = "none";

      renderQuestion();
    }}

    function changeMode() {{
      const modeSelect = document.getElementById("modeSelect");
      currentMode = modeSelect.value;
      modeSelect.blur();
      init();
    }}

    function resetQuiz() {{
      init();
    }}

    function renderQuestion() {{
      isAnswered = false;
      const q = questionsList[currentIndex];

      document.getElementById("qNumberBadge").textContent = `Q${{currentIndex + 1}} / ${{questionsList.length}} [No. ${{q.no}}]`;
      document.getElementById("posTag").textContent = q.pos;

      const pct = (currentIndex / questionsList.length) * 100;
      document.getElementById("progressBar").style.width = `${{Math.max(pct, 1)}}%`;

      const target = currentMode === "en_ja" ? q.word : q.meaning;
      document.getElementById("targetWord").textContent = target;

      const audioBtn = document.getElementById("btnSpeakWord");
      audioBtn.style.display = (currentMode === "en_ja") ? "inline-flex" : "none";

      currentChoicesData = generateDynamicChoices(q, currentMode);

      const grid = document.getElementById("choicesGrid");
      grid.innerHTML = "";

      currentChoicesData.choices.forEach((choice, idx) => {{
        const btn = document.createElement("button");
        btn.type = "button";
        btn.className = "choice-btn";

        const keySpan = document.createElement("span");
        keySpan.className = "choice-key";
        keySpan.textContent = CHOICE_KEYS[idx];

        const textSpan = document.createElement("span");
        textSpan.className = "choice-text";
        textSpan.textContent = choice;

        btn.appendChild(keySpan);
        btn.appendChild(textSpan);
        btn.addEventListener("click", () => handleAnswer(CHOICE_KEYS[idx], btn, q));
        grid.appendChild(btn);
      }});

      const feedbackPanel = document.getElementById("feedbackPanel");
      feedbackPanel.classList.remove("is-correct", "is-wrong");
      document.getElementById("feedbackIdle").style.display = "flex";
      document.getElementById("feedbackAnswered").style.display = "none";
    }}

    function handleAnswer(selectedKey, clickedBtn, q) {{
      if (isAnswered) return;
      isAnswered = true;

      if (document.activeElement && document.activeElement !== document.body) {{
        document.activeElement.blur();
      }}

      const isCorrect = (selectedKey === currentChoicesData.correctLetter);
      answerHistory[q.no] = isCorrect ? 'correct' : 'wrong';

      const allBtns = document.querySelectorAll(".choice-btn");
      allBtns.forEach((btn, idx) => {{
        btn.disabled = true;
        if (CHOICE_KEYS[idx] === currentChoicesData.correctLetter) {{
          btn.classList.add("correct");
        }} else if (btn !== clickedBtn) {{
          btn.classList.add("dimmed");
        }}
      }});

      const feedbackPanel = document.getElementById("feedbackPanel");
      const statusEl = document.getElementById("resultStatus");
      feedbackPanel.classList.remove("is-correct", "is-wrong");

      if (isCorrect) {{
        correctTotal++;
        document.getElementById("correctCount").textContent = correctTotal;
        feedbackPanel.classList.add("is-correct");
        statusEl.className = "result-status correct";
        statusEl.textContent = "正解";
      }} else {{
        wrongTotal++;
        document.getElementById("wrongCount").textContent = wrongTotal;
        clickedBtn.classList.add("wrong");
        wrongQuestions.push(q);
        feedbackPanel.classList.add("is-wrong");
        const correctAns = currentMode === "en_ja" ? q.meaning : q.word;
        statusEl.className = "result-status wrong";
        statusEl.textContent = `不正解 — 正解: [${{currentChoicesData.correctLetter}}] ${{correctAns}}`;
      }}

      const answeredCount = correctTotal + wrongTotal;
      const acc = answeredCount > 0 ? ((correctTotal / answeredCount) * 100).toFixed(1) : "0.0";
      document.getElementById("accuracyText").textContent = `${{acc}}%`;

      document.getElementById("expEn").textContent = q.example_en;
      document.getElementById("expJa").textContent = q.example_ja;
      document.getElementById("expNotes").textContent = q.notes;

      document.getElementById("feedbackIdle").style.display = "none";
      document.getElementById("feedbackAnswered").style.display = "flex";
    }}

    function nextQuestion() {{
      currentIndex++;
      if (currentIndex < questionsList.length) {{
        renderQuestion();
      }} else {{
        showResult();
      }}
    }}

    function showResult() {{
      document.getElementById("quizCard").style.display = "none";
      const resView = document.getElementById("resultView");
      resView.style.display = "flex";

      document.getElementById("progressBar").style.width = "100%";
      document.getElementById("finalScore").textContent = `${{correctTotal}} / ${{questionsList.length}}`;
      const acc = ((correctTotal / questionsList.length) * 100).toFixed(1);
      document.getElementById("finalAccuracy").textContent = `正答率: ${{acc}}%`;

      const btnRetry = document.getElementById("btnRetryWrong");
      if (wrongQuestions.length === 0) {{
        btnRetry.style.display = "none";
      }} else {{
        btnRetry.style.display = "inline-block";
        btnRetry.textContent = `間違えた${{wrongQuestions.length}}問のみ復習`;
      }}
    }}

    function retryWrongOnly() {{
      if (wrongQuestions.length === 0) return;
      questionsList = [...wrongQuestions];
      currentIndex = 0;
      correctTotal = 0;
      wrongTotal = 0;
      wrongQuestions = [];
      isAnswered = false;

      document.getElementById("correctCount").textContent = "0";
      document.getElementById("wrongCount").textContent = "0";
      document.getElementById("accuracyText").textContent = "0.0%";

      document.getElementById("quizCard").style.display = "flex";
      document.getElementById("resultView").style.display = "none";

      renderQuestion();
    }}

    function openJumpModal() {{
      const grid = document.getElementById("jumpGrid");
      grid.innerHTML = "";
      questionsList.forEach((q, idx) => {{
        const btn = document.createElement("button");
        btn.type = "button";
        btn.className = "grid-num-btn";
        btn.textContent = q.no;
        if (idx === currentIndex) btn.classList.add("current");
        if (answerHistory[q.no] === 'correct') btn.classList.add("answered-correct");
        if (answerHistory[q.no] === 'wrong') btn.classList.add("answered-wrong");
        btn.onclick = () => {{
          currentIndex = idx;
          document.getElementById("jumpModal").style.display = "none";
          showQuizTab();
          document.getElementById("quizCard").style.display = "flex";
          document.getElementById("resultView").style.display = "none";
          renderQuestion();
        }};
        grid.appendChild(btn);
      }});
      document.getElementById("jumpModal").style.display = "flex";
    }}

    function closeJumpModal(e) {{
      if (e.target.id === 'jumpModal') {{
        document.getElementById("jumpModal").style.display = "none";
      }}
    }}

    /* タブ切り替え */
    function showQuizTab() {{
      document.getElementById("quizArea").style.display = "flex";
      document.getElementById("wordbookArea").style.display = "none";
      document.getElementById("btnQuizTab").classList.add("btn-tab-active");
      document.getElementById("btnWordbookTab").classList.remove("btn-tab-active");
    }}

    function showWordbookTab() {{
      document.getElementById("quizArea").style.display = "none";
      document.getElementById("wordbookArea").style.display = "flex";
      document.getElementById("btnQuizTab").classList.remove("btn-tab-active");
      document.getElementById("btnWordbookTab").classList.add("btn-tab-active");
      filterWordList();
    }}

    function renderWordbookList(words) {{
      const container = document.getElementById("wordListContainer");
      container.innerHTML = "";
      words.forEach(w => {{
        const card = document.createElement("div");
        card.className = "word-card";

        const header = document.createElement("div");
        header.className = "word-header";

        const leftInfo = document.createElement("div");
        const noSpan = document.createElement("span");
        noSpan.style.cssText = "font-weight: 800; color: #1e3a8a; font-size: 0.85rem; margin-right: 0.45rem;";
        noSpan.textContent = `No.${{w.no}}`;

        const wordStrong = document.createElement("strong");
        wordStrong.style.cssText = "font-size: 1.1rem; color: #0f172a;";
        wordStrong.textContent = w.word;

        const posSpan = document.createElement("span");
        posSpan.style.cssText = "font-size: 0.78rem; background: #f1f5f9; padding: 0.15rem 0.45rem; border-radius: 4px; margin-left: 0.45rem; color: #475569;";
        posSpan.textContent = w.pos;

        leftInfo.appendChild(noSpan);
        leftInfo.appendChild(wordStrong);
        leftInfo.appendChild(posSpan);

        const speakBtn = document.createElement("button");
        speakBtn.type = "button";
        speakBtn.className = "btn-audio-sm";
        speakBtn.textContent = "発音";
        speakBtn.addEventListener("click", () => speakDirect(w.word));

        header.appendChild(leftInfo);
        header.appendChild(speakBtn);

        const meaningDiv = document.createElement("div");
        meaningDiv.style.cssText = "font-size: 0.95rem; font-weight: 700; color: #2563eb; margin-bottom: 0.3rem;";
        meaningDiv.textContent = w.meaning;

        const exEnDiv = document.createElement("div");
        exEnDiv.style.cssText = "font-size: 0.88rem; font-weight: 600; color: #334155; margin-bottom: 0.15rem;";
        exEnDiv.textContent = w.example_en;

        const exJaDiv = document.createElement("div");
        exJaDiv.style.cssText = "font-size: 0.82rem; color: #64748b; margin-bottom: 0.3rem;";
        exJaDiv.textContent = w.example_ja;

        const notesDiv = document.createElement("div");
        notesDiv.style.cssText = "font-size: 0.78rem; background: #f8fafc; padding: 0.3rem 0.55rem; border-radius: 4px; color: #475569;";
        notesDiv.textContent = w.notes;

        card.appendChild(header);
        card.appendChild(meaningDiv);
        card.appendChild(exEnDiv);
        card.appendChild(exJaDiv);
        card.appendChild(notesDiv);
        container.appendChild(card);
      }});
    }}

    function filterWordList() {{
      const q = document.getElementById("searchInput").value.toLowerCase();
      const filtered = ALL_WORDS.filter(w =>
        w.word.toLowerCase().includes(q) ||
        w.meaning.toLowerCase().includes(q) ||
        w.no.toString().includes(q) ||
        w.example_en.toLowerCase().includes(q) ||
        w.example_ja.toLowerCase().includes(q)
      );
      renderWordbookList(filtered);
    }}

    function speakDirect(text) {{
      if (!window.speechSynthesis) return;
      window.speechSynthesis.cancel();
      const u = new SpeechSynthesisUtterance(text);
      u.lang = 'en-US';
      u.rate = 0.9;
      window.speechSynthesis.speak(u);
    }}

    function speakText(text) {{
      speakDirect(text);
    }}

    function speakTargetWord() {{
      const q = questionsList[currentIndex];
      speakText(q.word);
    }}

    function speakSentence() {{
      const q = questionsList[currentIndex];
      speakText(q.example_en);
    }}

    window.addEventListener("keydown", (e) => {{
      if (e.ctrlKey || e.metaKey || e.altKey) return;

      const jumpModal = document.getElementById("jumpModal");
      if (jumpModal.style.display === "flex") {{
        if (e.key === "Escape") {{
          jumpModal.style.display = "none";
        }}
        return;
      }}

      if (document.getElementById("wordbookArea").style.display === "flex") return;
      if (document.getElementById("resultView").style.display === "flex") return;

      if (!isAnswered) {{
        const fullToHalf = {{'１':'1','２':'2','３':'3','４':'4','５':'5','６':'6','７':'7','８':'8','９':'9','０':'0'}};
        const normalizedKey = fullToHalf[e.key] || e.key;
        const index = CHOICE_KEYS.indexOf(normalizedKey);
        if (index !== -1) {{
          const btns = document.querySelectorAll(".choice-btn");
          if (btns[index]) btns[index].click();
        }}
      }} else {{
        if (e.key === "Enter" || e.key === " " || e.key === "ArrowRight") {{
          e.preventDefault();
          nextQuestion();
        }}
      }}
    }});

    init();
  </script>
</body>
</html>
'''

index_path = os.path.join(OUTPUT_DIR, "index.html")
with open(index_path, mode="w", encoding="utf-8") as f:
    f.write(html_content)
print("Saved updated index.html:", index_path)

for app_name in ["TOEIC_100Quiz_App.html", "TOEIC_100問10択クイズ_学習アプリ.html"]:
    shutil.copyfile(index_path, os.path.join(OUTPUT_DIR, app_name))
    print(f"Copied to {app_name}")
