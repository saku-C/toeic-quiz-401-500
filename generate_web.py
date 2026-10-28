# -*- coding: utf-8 -*-
"""
Web公開用 index.html 生成スクリプト
- 出題順: No.401 〜 No.500 (番号順で固定)
- 10択の選択肢: 毎回出題時/リセット時に完全にランダム生成！
- 単語帳一覧モード（検索・発音・全項目表示）
- Web Speech API ネイティブ発音再生
- 問題一覧ジャンプモーダル
- Googleスプレッドシート用CSV & Excel ダウンロード
"""

import os
import json
from quiz_data import words_data

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

all_words_json = json.dumps(words_data, ensure_ascii=False)

html_content = f'''<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>TOEIC 100問10択クイズ (No.401-500)</title>
  <meta name="description" content="単語帳 No.401〜500。出題は番号順。単語帳閲覧機能、ネイティブ音声・解説付き。">
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
      --bg: #f8fafc;
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

    body {{
      background: var(--bg);
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      padding: 1rem 0.75rem 3rem 0.75rem;
    }}

    .container {{
      max-width: 860px;
      margin: 0 auto;
      width: 100%;
    }}

    header {{
      background: var(--card-bg);
      padding: 1.1rem 1.25rem;
      border-radius: 1rem;
      box-shadow: var(--shadow-sm);
      margin-bottom: 1rem;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 0.75rem;
      border: 1px solid var(--border);
    }}

    .title-group h1 {{
      font-size: 1.25rem;
      font-weight: 800;
      color: #1e3a8a;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      letter-spacing: -0.01em;
    }}

    .title-group p {{
      font-size: 0.8rem;
      color: var(--text-muted);
      margin-top: 0.15rem;
    }}

    .top-badge {{
      display: inline-block;
      font-size: 0.7rem;
      background: #e0f2fe;
      color: #0369a1;
      padding: 0.15rem 0.5rem;
      border-radius: 9999px;
      font-weight: 700;
      margin-left: 0.25rem;
    }}

    .controls {{
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
      align-items: center;
    }}

    select, button.control-btn, a.control-btn {{
      padding: 0.45rem 0.8rem;
      border-radius: 0.5rem;
      border: 1px solid var(--border);
      background: var(--card-bg);
      color: var(--text-main);
      font-size: 0.825rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s ease;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 0.3rem;
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

    /* ダッシュボード */
    .dashboard {{
      background: var(--card-bg);
      border-radius: 1rem;
      padding: 0.9rem 1.25rem;
      margin-bottom: 1rem;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
    }}

    .stats-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.875rem;
      font-weight: 600;
    }}

    .stat-badge {{
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      padding: 0.2rem 0.6rem;
      border-radius: 9999px;
      font-size: 0.8rem;
    }}

    .badge-correct {{ background: var(--success-light); color: var(--success); }}
    .badge-wrong {{ background: var(--danger-light); color: var(--danger); }}
    .badge-accuracy {{ background: var(--primary-light); color: var(--primary); }}

    .progress-bar-bg {{
      height: 8px;
      background: var(--border);
      border-radius: 9999px;
      overflow: hidden;
    }}

    .progress-bar-fill {{
      height: 100%;
      background: linear-gradient(90deg, #2563eb, #3b82f6);
      width: 1%;
      transition: width 0.3s ease;
    }}

    /* クイズカード */
    .quiz-card {{
      background: var(--card-bg);
      border-radius: 1.25rem;
      padding: 1.75rem 1.5rem;
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
      position: relative;
    }}

    .question-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.75rem;
    }}

    .q-number {{
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--primary);
      background: var(--primary-light);
      padding: 0.3rem 0.75rem;
      border-radius: 0.5rem;
      cursor: pointer;
      transition: background 0.15s;
    }}
    .q-number:hover {{
      background: #dbeafe;
    }}

    .pos-tag {{
      font-size: 0.8rem;
      font-weight: 700;
      color: #475569;
      background: #f1f5f9;
      padding: 0.3rem 0.7rem;
      border-radius: 0.5rem;
    }}

    .target-wrapper {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.75rem;
      margin: 1rem 0 1.5rem 0;
    }}

    .target-word {{
      font-size: 2.25rem;
      font-weight: 800;
      color: var(--text-main);
      text-align: center;
      letter-spacing: -0.02em;
    }}

    .btn-audio {{
      background: #f1f5f9;
      border: 1px solid var(--border);
      padding: 0.35rem 0.85rem;
      height: 36px;
      border-radius: 18px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--primary);
      transition: all 0.2s;
      flex-shrink: 0;
    }}

    .btn-audio:hover {{
      background: var(--primary-light);
      border-color: var(--primary);
    }}

    /* 10択グリッド */
    .choices-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 0.65rem;
      margin-bottom: 1.25rem;
    }}

    @media (max-width: 640px) {{
      body {{
        padding: 0.5rem 0.5rem 2rem 0.5rem;
      }}
      .quiz-card {{
        padding: 1.25rem 1rem;
      }}
      .choices-grid {{
        grid-template-columns: 1fr;
        gap: 0.5rem;
      }}
      .target-word {{
        font-size: 1.85rem;
      }}
    }}

    .choice-btn {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      background: #ffffff;
      border: 2px solid var(--border);
      padding: 0.85rem 1rem;
      border-radius: 0.75rem;
      cursor: pointer;
      font-size: 0.95rem;
      font-weight: 500;
      text-align: left;
      transition: all 0.15s ease;
      color: var(--text-main);
      position: relative;
    }}

    .choice-btn:hover:not(:disabled) {{
      border-color: var(--primary);
      background: var(--primary-light);
      transform: translateY(-1px);
    }}

    .choice-key {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 28px;
      height: 28px;
      background: #f1f5f9;
      color: #475569;
      border-radius: 6px;
      font-size: 0.85rem;
      font-weight: 700;
      flex-shrink: 0;
    }}

    .choice-btn.correct {{
      border-color: var(--success) !important;
      background: var(--success-light) !important;
      color: var(--success) !important;
      font-weight: 700;
    }}
    .choice-btn.correct .choice-key {{
      background: var(--success);
      color: #fff;
    }}

    .choice-btn.wrong {{
      border-color: var(--danger) !important;
      background: var(--danger-light) !important;
      color: var(--danger) !important;
    }}
    .choice-btn.wrong .choice-key {{
      background: var(--danger);
      color: #fff;
    }}

    /* 解説エリア */
    .explanation-card {{
      background: #f8fafc;
      border-left: 4px solid var(--primary);
      padding: 1.1rem;
      border-radius: 0.5rem;
      margin-top: 1rem;
      display: none;
      animation: fadeIn 0.2s ease;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(4px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    .explanation-title {{
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--primary);
      margin-bottom: 0.4rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }}

    .example-en-row {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      margin-bottom: 0.25rem;
    }}

    .example-en {{
      font-size: 0.95rem;
      font-weight: 600;
      color: #1e293b;
    }}

    .btn-audio-sm {{
      background: #f1f5f9;
      border: 1px solid var(--border);
      padding: 0.25rem 0.6rem;
      border-radius: 6px;
      cursor: pointer;
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--primary);
      transition: all 0.2s;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }}
    .btn-audio-sm:hover {{
      background: var(--primary-light);
      border-color: var(--primary);
    }}

    .example-ja {{
      font-size: 0.875rem;
      color: #64748b;
      margin-bottom: 0.5rem;
    }}

    .notes-text {{
      font-size: 0.825rem;
      background: #f1f5f9;
      padding: 0.45rem 0.7rem;
      border-radius: 0.4rem;
      color: #334155;
    }}

    .action-row {{
      display: flex;
      justify-content: flex-end;
      align-items: center;
      margin-top: 1.25rem;
      gap: 0.75rem;
    }}

    .btn-next {{
      background: var(--primary);
      color: #ffffff;
      padding: 0.75rem 2rem;
      font-size: 1rem;
      font-weight: 700;
      border: none;
      border-radius: 0.75rem;
      cursor: pointer;
      display: none;
      transition: background 0.2s;
      width: 100%;
    }}

    @media (min-width: 641px) {{
      .btn-next {{
        width: auto;
      }}
    }}

    .btn-next:hover {{
      background: var(--primary-dark);
    }}

    /* リザルト画面 */
    .result-view {{
      display: none;
      text-align: center;
      padding: 3rem 1.5rem;
    }}

    .result-score {{
      font-size: 4rem;
      font-weight: 800;
      color: var(--primary);
      margin: 1rem 0;
    }}

    .result-actions {{
      display: flex;
      justify-content: center;
      gap: 0.75rem;
      margin-top: 2rem;
      flex-wrap: wrap;
    }}

    /* 単語帳一覧ビュー */
    .wordbook-view {{
      display: none;
    }}
    .search-box {{
      width: 100%;
      padding: 0.75rem 1rem;
      border-radius: 0.75rem;
      border: 1px solid var(--border);
      font-size: 0.95rem;
      margin-bottom: 1rem;
      outline: none;
    }}
    .search-box:focus {{
      border-color: var(--primary);
    }}
    .word-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 0.75rem;
      padding: 1rem;
      margin-bottom: 0.75rem;
      transition: transform 0.15s;
    }}
    .word-card:hover {{
      box-shadow: var(--shadow-sm);
    }}
    .word-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.4rem;
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
      padding: 1.5rem;
      box-shadow: var(--shadow-lg);
    }}
    .modal-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(48px, 1fr));
      gap: 0.5rem;
      margin-top: 1rem;
    }}
    .grid-num-btn {{
      height: 40px;
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
  </style>
</head>
<body>

  <div class="container">
    <header>
      <div class="title-group">
        <h1>TOEIC 100問10択クイズ</h1>
        <p>No. 401 〜 500 (出題順: 番号順)</p>
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
      <div class="dashboard" id="dashboard">
        <div class="stats-row">
          <div>
            <span>進捗: </span>
            <span id="progressText" style="font-weight: 700;">1 / 100</span>
            <span style="font-size: 0.75rem; color: var(--text-muted); margin-left: 0.3rem;">(番号順に出題)</span>
          </div>
          <div style="display: flex; gap: 0.4rem;">
            <span class="stat-badge badge-correct">○ <span id="correctCount">0</span></span>
            <span class="stat-badge badge-wrong">× <span id="wrongCount">0</span></span>
            <span class="stat-badge badge-accuracy">正答率: <span id="accuracyText">0.0%</span></span>
          </div>
        </div>
        <div class="progress-bar-bg">
          <div class="progress-bar-fill" id="progressBar"></div>
        </div>
      </div>

      <div class="quiz-card" id="quizCard">
        <div class="question-header">
          <span class="q-number" id="qNumberBadge" onclick="openJumpModal()" title="クリックして問題一覧を開く">Q1 / 100 [No. 401]</span>
          <div style="display: flex; gap: 0.4rem; align-items: center;">
            <select id="modeSelect" onchange="changeMode()" style="padding: 0.25rem 0.5rem; font-size: 0.8rem;">
              <option value="en_ja">英 → 日 (10択)</option>
              <option value="ja_en">日 → 英 (10択)</option>
            </select>
            <span class="pos-tag" id="posTag">動詞</span>
          </div>
        </div>

        <div class="target-wrapper">
          <div class="target-word" id="targetWord">cause</div>
          <button class="btn-audio" id="btnSpeakWord" title="単語の発音を聞く" onclick="speakTargetWord()">発音</button>
        </div>

        <div class="choices-grid" id="choicesGrid"></div>

        <div class="explanation-card" id="explanationCard">
          <div class="explanation-title">単語解説・例文</div>
          <div class="example-en-row">
            <div class="example-en" id="expEn">Heavy traffic is causing delays on Highway 18.</div>
            <button class="btn-audio-sm" id="btnSpeakSentence" title="例文の発音を聞く" onclick="speakSentence()">例文音声</button>
          </div>
          <div class="example-ja" id="expJa">18号線では交通渋滞により遅れが生じています。</div>
          <div class="notes-text" id="expNotes">名: cause「原因、理由、大義」</div>
        </div>

        <div class="action-row">
          <button class="btn-next" id="btnNext" onclick="nextQuestion()">次の問題へ (Enter)</button>
        </div>
      </div>

      <div class="quiz-card result-view" id="resultView">
        <h2>お疲れ様でした！クイズ終了</h2>
        <p style="color: var(--text-muted); margin-top: 0.5rem;">全100問の挑戦が完了しました！</p>
        
        <div class="result-score" id="finalScore">95 / 100</div>
        <p id="finalAccuracy" style="font-size: 1.25rem; font-weight: 600; color: #334155;">正答率: 95.0%</p>

        <div class="result-actions">
          <button class="btn-next" style="display: inline-block; width: auto;" onclick="retryWrongOnly()" id="btnRetryWrong">間違えた問題のみ復習</button>
          <button class="control-btn" style="padding: 0.75rem 1.5rem;" onclick="resetQuiz()">もう一度最初から</button>
        </div>
      </div>
    </div>

    <!-- 素の単語帳一覧エリア -->
    <div id="wordbookArea" class="wordbook-view">
      <div style="background: #ffffff; padding: 1.25rem; border-radius: 1rem; border: 1px solid var(--border); margin-bottom: 1rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem; flex-wrap: wrap; gap: 0.5rem;">
          <h2 style="font-size: 1.15rem; font-weight: 800; color: #1e3a8a;">単語帳一覧 (No.401 〜 500 全100語)</h2>
          <div style="display: flex; gap: 0.4rem; flex-wrap: wrap;">
            <a class="control-btn" href="https://docs.google.com/spreadsheets/d/1BaAIXt7jKJIoEdopA-uozzmqyQw_e2ePdSPwFk4MSac/edit?usp=sharing" target="_blank" rel="noopener">単語帳(スプレットシート)</a>
            <a class="control-btn" href="TOEIC_Words_401-500_List.csv" download>CSV保存</a>
            <a class="control-btn" href="TOEIC_Words_401-500_100Quiz.xlsx" download>Excel保存</a>
          </div>
        </div>
        <input type="text" id="searchInput" class="search-box" placeholder="単語・意味・例文を検索..." oninput="filterWordList()">
        <div id="wordListContainer"></div>
      </div>
    </div>
  </div>

  <!-- 問題一覧ジャンプモーダル -->
  <div class="modal-overlay" id="jumpModal" onclick="closeJumpModal(event)">
    <div class="modal-content" onclick="event.stopPropagation()">
      <div style="display: flex; justify-content: space-between; align-items: center;">
        <h3 style="font-size: 1.1rem; font-weight: 700;">問題一覧 (No.401 〜 500)</h3>
        <button class="control-btn" onclick="document.getElementById('jumpModal').style.display='none'">閉じる</button>
      </div>
      <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.3rem;">番号をクリックするとその問題に直接ジャンプします。（出題順: 番号順）</p>
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

    // 出題のたびに毎回ランダムで10択を生成する関数
    function generateDynamicChoices(targetItem, mode) {{
      const isEnJa = (mode === "en_ja");
      const correctAnswer = isEnJa ? targetItem.meaning : targetItem.word;
      
      // 他の単語99語からランダムにサンプリング
      const others = ALL_WORDS.filter(w => w.no !== targetItem.no);
      // シャッフル
      const shuffledOthers = [...others].sort(() => Math.random() - 0.5);
      
      const dummyAnswers = [];
      for (const item of shuffledOthers) {{
        const ans = isEnJa ? item.meaning : item.word;
        if (ans !== correctAnswer && !dummyAnswers.includes(ans)) {{
          dummyAnswers.push(ans);
        }}
        if (dummyAnswers.length === 9) break;
      }}
      
      // 正解1つ + ダミー9つ
      const choices = [correctAnswer, ...dummyAnswers];
      // 選択肢の並び順をランダムシャッフル！
      choices.sort(() => Math.random() - 0.5);
      
      const correctLetter = CHOICE_KEYS[choices.indexOf(correctAnswer)];
      
      return {{
        choices: choices,
        correctLetter: correctLetter
      }};
    }}

    function init() {{
      // 出題順は番号順 (401〜500)
      questionsList = [...ALL_WORDS];
      currentIndex = 0;
      correctTotal = 0;
      wrongTotal = 0;
      wrongQuestions = [];
      isAnswered = false;
      answerHistory = {{}};
      
      document.getElementById("quizCard").style.display = "block";
      document.getElementById("resultView").style.display = "none";
      
      renderQuestion();
    }}

    function changeMode() {{
      currentMode = document.getElementById("modeSelect").value;
      init();
    }}

    function resetQuiz() {{
      init();
    }}

    function renderQuestion() {{
      isAnswered = false;
      const q = questionsList[currentIndex];
      
      document.getElementById("progressText").textContent = `${{currentIndex + 1}} / ${{questionsList.length}}`;
      document.getElementById("qNumberBadge").textContent = `Q${{currentIndex + 1}} / ${{questionsList.length}} [No. ${{q.no}}]`;
      document.getElementById("posTag").textContent = q.pos;
      
      const pct = ((currentIndex) / questionsList.length) * 100;
      document.getElementById("progressBar").style.width = `${{Math.max(pct, 2)}}%`;
      
      const target = currentMode === "en_ja" ? q.word : q.meaning;
      document.getElementById("targetWord").textContent = target;

      const audioBtn = document.getElementById("btnSpeakWord");
      if (currentMode === "en_ja") {{
        audioBtn.style.display = "inline-flex";
      }} else {{
        audioBtn.style.display = "none";
      }}

      // 毎回ランダムに10択を生成
      currentChoicesData = generateDynamicChoices(q, currentMode);

      const grid = document.getElementById("choicesGrid");
      grid.innerHTML = "";
      
      currentChoicesData.choices.forEach((choice, idx) => {{
        const btn = document.createElement("button");
        btn.className = "choice-btn";
        btn.innerHTML = `<span class="choice-key">${{CHOICE_KEYS[idx]}}</span><span>${{choice}}</span>`;
        btn.onclick = () => handleAnswer(CHOICE_KEYS[idx], btn, q);
        grid.appendChild(btn);
      }});

      document.getElementById("explanationCard").style.display = "none";
      document.getElementById("btnNext").style.display = "none";
    }}

    function handleAnswer(selectedKey, clickedBtn, q) {{
      if (isAnswered) return;
      isAnswered = true;

      const isCorrect = (selectedKey === currentChoicesData.correctLetter);
      answerHistory[q.no] = isCorrect ? 'correct' : 'wrong';

      const allBtns = document.querySelectorAll(".choice-btn");
      allBtns.forEach((btn, idx) => {{
        btn.disabled = true;
        if (CHOICE_KEYS[idx] === currentChoicesData.correctLetter) {{
          btn.classList.add("correct");
        }}
      }});

      if (isCorrect) {{
        correctTotal++;
        document.getElementById("correctCount").textContent = correctTotal;
      }} else {{
        wrongTotal++;
        document.getElementById("wrongCount").textContent = wrongTotal;
        clickedBtn.classList.add("wrong");
        wrongQuestions.push(q);
      }}

      const answeredCount = correctTotal + wrongTotal;
      const acc = answeredCount > 0 ? ((correctTotal / answeredCount) * 100).toFixed(1) : "0.0";
      document.getElementById("accuracyText").textContent = `${{acc}}%`;

      document.getElementById("expEn").textContent = q.example_en;
      document.getElementById("expJa").textContent = q.example_ja;
      document.getElementById("expNotes").textContent = q.notes;
      document.getElementById("explanationCard").style.display = "block";

      const nextBtn = document.getElementById("btnNext");
      nextBtn.style.display = "inline-block";
      nextBtn.focus();
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
      resView.style.display = "block";
      
      document.getElementById("progressBar").style.width = "100%";
      document.getElementById("progressText").textContent = `${{questionsList.length}} / ${{questionsList.length}}`;
      
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
      
      document.getElementById("quizCard").style.display = "block";
      document.getElementById("resultView").style.display = "none";
      
      renderQuestion();
    }}

    function openJumpModal() {{
      const grid = document.getElementById("jumpGrid");
      grid.innerHTML = "";
      questionsList.forEach((q, idx) => {{
        const btn = document.createElement("button");
        btn.className = "grid-num-btn";
        btn.textContent = q.no;
        if (idx === currentIndex) btn.classList.add("current");
        if (answerHistory[q.no] === 'correct') btn.classList.add("answered-correct");
        if (answerHistory[q.no] === 'wrong') btn.classList.add("answered-wrong");
        btn.onclick = () => {{
          currentIndex = idx;
          document.getElementById("jumpModal").style.display = "none";
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
      document.getElementById("quizArea").style.display = "block";
      document.getElementById("wordbookArea").style.display = "none";
      document.getElementById("btnQuizTab").classList.add("btn-tab-active");
      document.getElementById("btnWordbookTab").classList.remove("btn-tab-active");
    }}

    function showWordbookTab() {{
      document.getElementById("quizArea").style.display = "none";
      document.getElementById("wordbookArea").style.display = "block";
      document.getElementById("btnQuizTab").classList.remove("btn-tab-active");
      document.getElementById("btnWordbookTab").classList.add("btn-tab-active");
      renderWordbookList(ALL_WORDS);
    }}

    function renderWordbookList(words) {{
      const container = document.getElementById("wordListContainer");
      container.innerHTML = "";
      words.forEach(w => {{
        const card = document.createElement("div");
        card.className = "word-card";
        card.innerHTML = `
          <div class="word-header">
            <div>
              <span style="font-weight: 800; color: #1e3a8a; font-size: 0.9rem; margin-right: 0.5rem;">No.${{w.no}}</span>
              <strong style="font-size: 1.2rem; color: #0f172a;">${{w.word}}</strong>
              <span style="font-size: 0.8rem; background: #f1f5f9; padding: 0.2rem 0.5rem; border-radius: 4px; margin-left: 0.5rem; color: #475569;">${{w.pos}}</span>
            </div>
            <button class="btn-audio-sm" onclick="speakDirect('${{w.word}}')">発音</button>
          </div>
          <div style="font-size: 1rem; font-weight: 700; color: #2563eb; margin-bottom: 0.4rem;">${{w.meaning}}</div>
          <div style="font-size: 0.9rem; font-weight: 600; color: #334155; margin-bottom: 0.2rem;">${{w.example_en}}</div>
          <div style="font-size: 0.85rem; color: #64748b; margin-bottom: 0.4rem;">${{w.example_ja}}</div>
          <div style="font-size: 0.8rem; background: #f8fafc; padding: 0.35rem 0.6rem; border-radius: 4px; color: #475569;">${{w.notes}}</div>
        `;
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
      if (document.getElementById("wordbookArea").style.display === "block") return;
      if (!isAnswered) {{
        const fullToHalf = {{'１':'1','２':'2','３':'3','４':'4','５':'5','６':'6','７':'7','８':'8','９':'9','０':'0'}};
        const normalizedKey = fullToHalf[e.key] || e.key;
        const index = CHOICE_KEYS.indexOf(normalizedKey);
        if (index !== -1) {{
          const btns = document.querySelectorAll(".choice-btn");
          if (btns[index]) btns[index].click();
        }}
      }} else {{
        if (e.key === "Enter" || e.key === " ") {{
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
