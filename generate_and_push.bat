@echo off
REM ビジ法3級サイト自動更新バッチファイル
REM 毎日AM0:10に実行される想定

echo ========================================
echo ビジ法3級サイト自動更新開始
echo 実行時刻: %date% %time%
echo ========================================

REM 作業ディレクトリに移動（GitHubリポジトリのクローン先）
cd /d "C:\Users\%USERNAME%\Desktop\bizlaw-site"

REM Git設定確認
git config --global user.email "your-email@example.com"
git config --global user.name "Your Name"

REM 最新のリモート状態を取得
echo リモートリポジトリから最新状態を取得中...
git fetch origin main

REM Python仮想環境をアクティブ化
echo Python仮想環境をアクティブ化中...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo エラー: Python仮想環境のアクティブ化に失敗しました
    goto :error
)

REM 問題生成スクリプト実行
echo 問題を生成中...
python scripts\generate_questions.py
if errorlevel 1 (
    echo エラー: 問題生成に失敗しました
    goto :error
)

REM 体験談生成スクリプト実行
echo 体験談を生成中...
python scripts\generate_story.py
if errorlevel 1 (
    echo エラー: 体験談生成に失敗しました
    goto :error
)

REM 仮想環境を非アクティブ化
deactivate

REM 生成されたファイルをGitに追加
echo 生成されたファイルをGitに追加中...
git add data\

REM 変更がない場合はスキップ
git diff --staged --quiet
if not errorlevel 1 (
    echo 変更がないため、処理をスキップします
    goto :success
)

REM コミット
echo コミット中...
git commit -m "自動生成: %date% %time%の問題と体験談"
if errorlevel 1 (
    echo エラー: コミットに失敗しました
    goto :error
)

REM プッシュ
echo GitHub Pagesにプッシュ中...
git push origin main
if errorlevel 1 (
    echo エラー: プッシュに失敗しました
    goto :error
)

:success
echo ========================================
echo 自動更新が正常に完了しました
echo 完了時刻: %date% %time%
echo ========================================
exit /b 0

:error
echo ========================================
echo 自動更新でエラーが発生しました
echo エラー時刻: %date% %time%
echo ========================================
exit /b 1
