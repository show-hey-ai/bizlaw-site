@echo off
cd /d C:\Users\user\Desktop\bizlaw-site
echo 現在のディレクトリ: %CD%
echo.
echo Pythonサーバーを起動します...
python -m http.server 8000
pause