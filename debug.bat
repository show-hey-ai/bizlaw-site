@echo off
echo ========================================
echo ビジネス法務検定3級 - デバッグモード
echo ========================================
echo.

echo [1] 現在のディレクトリを確認...
cd /d "%~dp0"
echo 現在のディレクトリ: %CD%
echo.

echo [2] ディレクトリの内容を確認...
echo.
dir /b
echo.

echo [3] Pythonのバージョンを確認...
python --version
if %errorlevel% neq 0 (
    echo Pythonが見つかりません！
    echo.
    echo PATHを確認中...
    echo %PATH%
    echo.
    pause
    exit /b 1
)
echo.

echo [4] server.pyファイルの存在を確認...
if exist server.py (
    echo server.py が見つかりました。
) else (
    echo エラー: server.py が見つかりません！
    pause
    exit /b 1
)
echo.

echo [5] ポート8080の使用状況を確認...
netstat -ano | findstr :8080
if %errorlevel% equ 0 (
    echo ポート8080は使用中です。
) else (
    echo ポート8080は利用可能です。
)
echo.

echo [6] サーバーを起動します...
echo コマンド: python server.py
echo.
python server.py
pause
