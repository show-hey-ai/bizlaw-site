@echo off
echo ========================================
echo ビジネス法務検定3級 毎日学習サイト
echo ========================================
echo.

cd /d "%~dp0"

:: Node.jsがインストールされているか確認
where node >nul 2>&1
if %errorlevel% neq 0 (
    echo Node.jsがインストールされていません。
    echo Pythonサーバーを使用します...
    echo.
    goto :python_server
)

echo Node.jsサーバーを起動します...
npx http-server . -p 8080 -o
goto :end

:python_server
:: Pythonがインストールされているか確認
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo エラー: PythonもNode.jsもインストールされていません。
    echo どちらかをインストールしてください。
    pause
    exit /b 1
)

echo Pythonサーバーを起動します...
start cmd /k "python -m http.server 8080"
timeout /t 3 /nobreak >nul
start http://localhost:8080

:end
echo.
echo サーバーが起動しました！
echo URL: http://localhost:8080
pause
