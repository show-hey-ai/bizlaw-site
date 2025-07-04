@echo off
echo ====================================
echo Bizlaw Site ローカルテストサーバー
echo ====================================
echo.
echo サイトをローカルでテストします
echo ブラウザが自動的に開きます
echo.
echo Ctrl+C で終了できます
echo.

cd /d "C:\Users\user\Desktop\bizlaw-site"
python fix\test_server.py
