@echo off
echo ビジネス法務検定3級 毎日学習サイトを起動します...
echo.
echo ローカルサーバーを起動中...
start /B python server.py
echo.
echo 3秒後にブラウザで開きます...
timeout /t 3 /nobreak > nul
start http://localhost:8080
echo.
echo サーバーを停止するには、このウィンドウで Ctrl+C を押してください。
pause > nul
