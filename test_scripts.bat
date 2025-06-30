@echo off
REM テスト用バッチファイル - 手動でスクリプトを実行する

echo ========================================
echo ビジ法3級サイト テスト実行
echo 実行時刻: %date% %time%
echo ========================================

REM 作業ディレクトリに移動
cd /d "C:\Users\%USERNAME%\Desktop\bizlaw-site"

echo 現在のディレクトリ: %cd%

REM Python仮想環境をアクティブ化
echo Python仮想環境をアクティブ化中...
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
    echo 仮想環境アクティブ化完了
) else (
    echo 仮想環境が見つかりません。作成します...
    python -m venv venv
    call venv\Scripts\activate.bat
    pip install requests
)

REM Gemini CLIの確認
echo Gemini CLIの確認中...
gemini --version
if errorlevel 1 (
    echo エラー: Gemini CLIが見つかりません
    echo npm install -g @google/generative-ai-cli でインストールしてください
    echo その後 gemini auth で認証してください
    pause
    exit /b 1
)

REM 問題生成テスト
echo 問題生成テスト中...
python scripts\generate_questions.py
if errorlevel 1 (
    echo エラー: 問題生成に失敗しました
    pause
    exit /b 1
)

REM 体験談生成テスト
echo 体験談生成テスト中...
python scripts\generate_story.py
if errorlevel 1 (
    echo エラー: 体験談生成に失敗しました
    pause
    exit /b 1
)

REM 生成されたファイルを確認
echo 生成されたファイルを確認中...
dir data\*.json

echo ========================================
echo テスト実行完了！
echo dataフォルダにJSONファイルが生成されていれば成功です
echo ========================================

pause
