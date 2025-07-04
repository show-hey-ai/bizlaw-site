@echo off
echo ====================================
echo 過去のデータ一括生成スクリプト
echo ====================================

cd /d "C:\Users\user\Desktop\bizlaw-site"

REM Check if GOOGLE_API_KEY is set
if "%GOOGLE_API_KEY%"=="" (
    echo エラー: GOOGLE_API_KEY環境変数が設定されていません
    echo まず fix\setup_api_key.bat を実行してAPIキーを設定してください
    pause
    exit /b 1
)

REM Activate virtual environment
echo Python仮想環境をアクティベート中...
call venv\Scripts\activate.bat

REM 過去5日分のデータを生成
echo 過去5日分のデータを生成します...
echo.

for /L %%i in (1,1,5) do (
    echo %%i日前のデータを生成中...
    python fix\generate_past_questions.py %%i
    python fix\generate_past_story.py %%i
    echo.
    REM API制限を避けるため少し待機
    timeout /t 2 /nobreak > nul
)

echo.
echo 生成完了！
echo.
echo 生成されたファイル:
dir data\*.json /b /o-d

deactivate
pause
