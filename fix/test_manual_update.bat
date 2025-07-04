@echo off
echo ====================================
echo Bizlaw Site Manual Update Test
echo ====================================

cd /d "C:\Users\user\Desktop\bizlaw-site"

REM Check if GOOGLE_API_KEY is set
if "%GOOGLE_API_KEY%"=="" (
    echo エラー: GOOGLE_API_KEY環境変数が設定されていません
    echo まず fix\setup_api_key.bat を実行してAPIキーを設定してください
    pause
    exit /b 1
)

echo APIキー: %GOOGLE_API_KEY:~0,10%... (最初の10文字のみ表示)

REM Activate virtual environment
echo Python仮想環境をアクティベート中...
call venv\Scripts\activate.bat

REM Test question generation
echo.
echo 問題生成スクリプトのテスト実行...
python scripts\generate_questions.py

REM Test story generation
echo.
echo 体験談生成スクリプトのテスト実行...
python scripts\generate_story.py

REM Show generated files
echo.
echo 生成されたファイル:
dir data\*.json /b /o-d | head -10

deactivate
pause
