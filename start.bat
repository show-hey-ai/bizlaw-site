@echo off
echo ========================================
echo ビジネス法務検定3級 毎日学習サイト
echo ========================================
echo.

:: 現在のディレクトリを確認
cd /d "%~dp0"
echo 現在のディレクトリ: %CD%
echo.

:: Pythonがインストールされているか確認
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo エラー: Pythonがインストールされていません。
    echo Pythonをインストールしてから再実行してください。
    echo.
    pause
    exit /b 1
)

:: 既存のPythonサーバープロセスを確認
echo ポート8080の使用状況を確認中...
netstat -ano | findstr :8080 >nul 2>&1
if %errorlevel% equ 0 (
    echo.
    echo 警告: ポート8080は既に使用されています。
    echo 既存のサーバーを停止するか、別のポートを使用してください。
    echo.
    choice /C YN /M "続行しますか？"
    if errorlevel 2 exit /b 1
)

:: サーバーを起動
echo ローカルサーバーを起動します...
echo.

:: 新しいウィンドウでサーバーを起動
start "Bizlaw Server" cmd /k "python server.py"

:: サーバーの起動を待つ
echo サーバーの起動を待っています...
timeout /t 3 /nobreak >nul

:: ブラウザで開く
echo.
echo ブラウザでサイトを開きます...
start http://localhost:8080

echo.
echo ========================================
echo サーバーが起動しました！
echo URL: http://localhost:8080
echo.
echo サーバーを停止するには:
echo 1. 「Bizlaw Server」ウィンドウで Ctrl+C を押す
echo 2. または、ウィンドウを閉じる
echo ========================================
echo.
echo このウィンドウは閉じても構いません。
pause
