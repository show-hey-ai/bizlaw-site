# Bizlaw Site - ビジネス法務検定3級 毎日学習サイト

毎日新しいビジネス法務検定3級の問題と合格体験談を自動生成・公開するWebサイトです。

## 概要

このサイトは、ビジネス法務検定3級の学習者向けに、毎日10問の○×問題と合格体験談を提供します。Google Gemini APIを使用して自動的にコンテンツを生成し、GitHub Pagesで公開しています。

## 機能

- 📝 毎日10問の○×問題（解説付き）
- 💪 日替わりの合格体験談
- 📂 過去30日分の問題アーカイブ
- 🌐 レスポンシブデザイン
- 🤖 自動更新（毎日6:00 AM）

## 技術スタック

- **フロントエンド**: HTML, CSS, JavaScript
- **バックエンド**: Python 3.x
- **AI**: Google Gemini API
- **ホスティング**: GitHub Pages
- **自動化**: Windows Task Scheduler + Batch Scripts

## ディレクトリ構造

```
bizlaw-site/
├── data/                        # 生成されたJSONファイル
│   ├── questions_YYYYMMDD.json  # 各日の問題（10問）
│   └── story_YYYYMMDD.json      # 各日の体験談
├── scripts/                     # Python生成スクリプト
│   ├── generate_questions.py    # 問題生成
│   └── generate_story.py        # 体験談生成
├── fix/                         # 修正・メンテナンス用
│   └── README_FIX.md           # トラブルシューティング
├── generate_and_push.bat       # 自動更新スクリプト
├── index.html                  # メインページ
└── requirements.txt            # Python依存関係
```

## セットアップ

### 1. リポジトリのクローン

```bash
git clone https://github.com/show-hey-ai/bizlaw-site.git
cd bizlaw-site
```

### 2. Python環境のセットアップ

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Google Gemini APIキーの設定

```bash
setx GOOGLE_API_KEY "your-api-key-here"
```

### 4. 自動更新の設定

Windows Task Schedulerで`generate_and_push.bat`を毎日6:00 AMに実行するよう設定

## 使用方法

### 手動でコンテンツを生成

```bash
# Python仮想環境をアクティベート
venv\Scripts\activate

# 問題を生成
python scripts\generate_questions.py

# 体験談を生成
python scripts\generate_story.py
```

### 自動更新スクリプトの実行

```bash
generate_and_push.bat
```

## トラブルシューティング

問題が発生した場合は、`fix/README_FIX.md`を参照してください。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## 貢献

プルリクエストを歓迎します。大きな変更を行う場合は、まずissueを開いて変更内容を議論してください。

## 作者

Show Hey AI

## リンク

- [ライブサイト](https://show-hey-ai.github.io/bizlaw-site/)
- [問題の報告](https://github.com/show-hey-ai/bizlaw-site/issues)
