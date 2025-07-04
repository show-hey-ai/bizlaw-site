#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ローカルテストサーバー
サイトが正しく表示されるかテストするため
"""

import http.server
import socketserver
import os
import webbrowser
from threading import Timer

PORT = 8000

def open_browser():
    """ブラウザを開く"""
    webbrowser.open(f'http://localhost:{PORT}')

if __name__ == "__main__":
    # bizlaw-siteディレクトリに移動
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    Handler = http.server.SimpleHTTPRequestHandler
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"サーバーを起動しました: http://localhost:{PORT}")
        print("Ctrl+C で終了します")
        
        # 1秒後にブラウザを開く
        Timer(1, open_browser).start()
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nサーバーを停止しました")
