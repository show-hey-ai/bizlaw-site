@echo off
echo ====================================
echo Google API Key Setup Script
echo ====================================
echo.
echo このスクリプトはGoogle Gemini APIキーを設定します。
echo.
echo 1. Google AI Studio (https://aistudio.google.com/app/apikey) にアクセス
echo 2. 新しいAPIキーを作成またはコピー
echo 3. 下記にAPIキーを貼り付けてください
echo.
set /p API_KEY="APIキーを入力してください: "

if "%API_KEY%"=="" (
    echo エラー: APIキーが入力されていません
    pause
    exit /b 1
)

echo.
echo APIキーを環境変数に設定しています...
setx GOOGLE_API_KEY "%API_KEY%"

echo.
echo APIキーが設定されました！
echo 新しいコマンドプロンプトまたはPowerShellウィンドウで有効になります。
echo.
pause
