# 軽量なPythonスリムイメージを使用
FROM python:3.12-slim

# 作業ディレクトリ
WORKDIR /app

# アプリケーションファイルをコピー
COPY index.html server.py ./
COPY TOEIC_Words_401-500_100Quiz.xlsx ./
COPY TOEIC_Words_401-500_List.csv ./
COPY TOEIC_100Quiz_EN_to_JA.csv ./
COPY TOEIC_100Quiz_JA_to_EN.csv ./

# Cloud Runのデフォルトポート環境変数 (8080)
ENV PORT=8080

# サーバー起動
CMD ["python", "server.py"]
