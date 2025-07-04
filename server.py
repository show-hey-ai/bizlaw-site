import http.server
import socketserver
import os

# ポート番号
PORT = 8080

# ディレクトリをbizlaw-siteに変更
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# サーバーの設定
Handler = http.server.SimpleHTTPRequestHandler

# MIMEタイプの設定を追加
Handler.extensions_map.update({
    '.js': 'application/javascript',
    '.json': 'application/json',
    '.css': 'text/css',
    '.html': 'text/html',
})

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"サーバーが起動しました: http://localhost:{PORT}")
        print("Ctrl+C で停止します")
        httpd.serve_forever()
except OSError:
    print(f"エラー: ポート {PORT} は既に使用されています。")
    print("別のポート番号を試すか、既存のプロセスを終了してください。")
except KeyboardInterrupt:
    print("\nサーバーを停止しました。")
