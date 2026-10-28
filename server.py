# -*- coding: utf-8 -*-
"""
Web公開用サーバー・Cloud Run対応サーバー (Python標準ライブラリのみ使用)
Cloud Runの PORT 環境変数に対応
"""

import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler

class CustomHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # キャッシュ制御とCORS設定
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-cache, must-revalidate")
        super().end_headers()

def run_server():
    port = int(os.environ.get("PORT", 8080))
    server_address = ("", port)
    
    # 静的ファイルのディレクトリをスクリプトと同じ場所に設定
    web_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(web_dir)
    
    httpd = HTTPServer(server_address, CustomHandler)
    print(f"Server running on port {port} (Serving {web_dir})")
    print(f"Local URL: http://localhost:{port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
        httpd.server_close()

if __name__ == "__main__":
    run_server()
