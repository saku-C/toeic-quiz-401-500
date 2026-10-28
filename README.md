# TOEIC 100問10択クイズ (No. 401 - 500)

単語帳 No.401〜500の重要単語を学習できる100問10択クイズWebアプリです。

## 特徴
- **出題順**: No.401 〜 No.500（番号順）
- **10択クイズ**: 正解1つ＋ダミー9択
- **ネイティブ音声**: Web Speech APIによる単語・例文の発音再生
- **問題一覧ジャンプ**: 1〜100問の進捗と正誤がひと目で分かり、好きな問題へ直接移動可能
- **間違えた問題の復習機能**: 不正解になった問題だけをやり直す集中モード
- **スプレッドシート（Excel / CSV）ダウンロード**: 画面上部からファイルを直接保存可能

---

## Webへのデプロイ方法

### 方法1: GitHub Pages（推奨・無料・最も簡単）
1. GitHubで新しい公開リポジトリ（例: `toeic-quiz`）を作成
2. `index.html` および関連ファイルをプッシュ
3. リポジトリの `Settings` > `Pages` で、Sourceを `Deploy from a branch`、Branchを `main` / `root` に設定
4. 数分で公開URL（`https://<ユーザー名>.github.io/toeic-quiz/`）が発行されます。

---

### 方法2: Google Cloud Run にデプロイ
1. Google Cloud SDK (`gcloud`) をインストール
2. ターミナルでログインとプロジェクト設定:
   ```bash
   gcloud auth login
   gcloud config set project <YOUR_PROJECT_ID>
   ```
3. このディレクトリで以下を実行（Dockerfileから自動ビルド＆デプロイ）:
   ```bash
   gcloud run deploy toeic-quiz --source . --platform managed --region asia-northeast1 --allow-unauthenticated
   ```
4. デプロイ完了後、`https://toeic-quiz-xxxxxx.a.run.app` のような公開URLが発行されます。

---

### 方法3: 今すぐローカルネットワーク（Wi-Fi）でスマホから解く
同じWi-Fi環境にあるスマホからすぐにアクセスできます。
1. PCのターミナルでサーバーを起動:
   ```bash
   python server.py
   ```
2. スマホのブラウザ（Safari / Chrome）で以下を開く:
   ```text
   http://192.168.10.20:8080
   ```
