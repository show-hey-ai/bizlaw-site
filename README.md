# Bizlaw Site - ビジネス法務検定3級 毎日学習サイト

毎日新しいビジネス法務検定3級の問題と合格体験談、励ましの名言を自動生成・公開するWebサイトです。

## 🌟 概要

このサイトは、ビジネス法務検定3級の学習者向けに、以下のコンテンツを毎日自動更新で提供します：

- 📝 **10問の○×問題**（解説付き）
- ✨ **日替わりの名言**（偉人の名言で学習のモチベーションアップ）
- 💪 **合格体験談**（励みになる体験談を毎日更新）
- 📚 **過去の問題アーカイブ**（蓄積されたすべての過去問題にアクセス可能）
- 🤖 **AI学習サポートチャット**（Google Gemini API使用）

## 🚀 最新アップデート (2025.07.04)

### 主な変更点
- ✅ **モダンUIデザイン**: 絵文字を削除し、プロフェッショナルなデザインに刷新
- ✅ **フォント改善**: Google Fonts（Inter + Noto Sans JP）を採用
- ✅ **過去問題のトグル機能**: 日付をクリックで開閉可能に
- ✅ **AIチャット強化**: 複数回の会話履歴を正しく管理
- ✅ **アニメーション追加**: スムーズなホバーエフェクトとトランジション
- ✅ **レスポンシブデザイン**: すべてのデバイスで最適な表示

## 🎨 デザインの特徴

- **ダークテーマ**: 目に優しい配色で長時間の学習をサポート
- **モダンなタイポグラフィ**: Inter（英語）とNoto Sans JP（日本語）の組み合わせ
- **インタラクティブUI**: ホバーエフェクトやアニメーションで使いやすさを向上
- **アクセシビリティ**: 高コントラストで読みやすいテキスト
- **プロフェッショナルデザイン**: ビジネス学習に相応しい洗練された外観

## 📁 ディレクトリ構造

```
bizlaw-site/
├── index.html                   # メインWebページ
├── data/                        # 生成されたJSONデータ
│   ├── questions_YYYYMMDD.json  # 各日の問題（10問）
│   ├── story_YYYYMMDD.json      # 各日の体験談
│   └── quote_YYYYMMDD.json      # 各日の名言
├── scripts/                     # Python生成スクリプト
│   ├── generate_questions.py    # 問題生成
│   ├── generate_story.py        # 体験談生成
│   └── generate_quote.py        # 名言生成
├── generate_and_push.bat       # 自動更新スクリプト
└── requirements.txt            # Python依存関係
```

## 🛠️ セットアップ

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

#### 方法1: 環境変数として設定（推奨）
```bash
setx GOOGLE_API_KEY "your-api-key-here"
```

#### 方法2: HTMLファイルに直接設定
`index.html`内の以下の行を編集：
```javascript
const GEMINI_API_KEY = 'your-api-key-here';
```

APIキーの取得：[Google AI Studio](https://makersuite.google.com/app/apikey)

## 🎯 機能詳細

### 1. 今日の名言
- 偉人の名言を日替わりで表示
- 努力、目的達成、夢に関する名言を厳選
- 学習に活かせる教訓を提供
- 洗練された引用符デザイン

### 2. 今日の問題（10問）
- ビジネス法務に関する○×問題
- クリックで答えと解説を表示
- 実務に役立つ知識を厳選
- ホバー時のアニメーションで操作性向上

### 3. 過去の問題
- 日付ボタンをクリックで問題を表示/非表示
- アクティブな日付はハイライト表示
- 復習に最適な設計
- スムーズなトグルアニメーション

### 4. 合格体験記
- モチベーション向上のための体験談
- 毎日異なるストーリーを自動生成
- リアルな学習体験を共有

### 5. AI学習サポート
- ビジネス法務に関する質問に即座に回答
- 会話履歴を保持し、文脈を理解した応答
- Google Gemini APIによる高度な対話
- 専門用語を分かりやすく解説

## 🔧 使用方法

### ローカルでの実行
```bash
# index.htmlをブラウザで開く
start index.html
```

### 手動でのコンテンツ生成
```bash
# 仮想環境をアクティベート
venv\Scripts\activate

# 各コンテンツを生成
python scripts\generate_questions.py
python scripts\generate_story.py
python scripts\generate_quote.py
```

### 自動更新の設定
Windows Task Schedulerで`generate_and_push.bat`を毎日6:00 AMに実行するよう設定

## 📊 データフォーマット

### questions_YYYYMMDD.json
```json
{
  "questions": [
    {
      "id": 1,
      "question": "質問文",
      "answer": true/false,
      "explanation": "解説文"
    }
  ],
  "generated_date": "YYYY-MM-DD",
  "topic_areas": ["分野1", "分野2"]
}
```

### story_YYYYMMDD.json
```json
{
  "story": {
    "content": "体験談の内容",
    "tone": "文体",
    "themes": ["テーマ1", "テーマ2"]
  },
  "generated_date": "YYYY-MM-DD"
}
```

### quote_YYYYMMDD.json
```json
{
  "author": "著者名",
  "quote_ja": "日本語の名言",
  "quote_original": "原文（あれば）",
  "lesson": "学習への教訓",
  "generated_date": "YYYY-MM-DD"
}
```

## 🐛 トラブルシューティング

### よくある問題

1. **APIキーエラー**
   - 環境変数`GOOGLE_API_KEY`が設定されているか確認
   - 新しいコマンドプロンプトで実行しているか確認

2. **データが表示されない**
   - `data/`フォルダに該当日付のJSONファイルがあるか確認
   - ブラウザのコンソール（F12）でエラーを確認
   - JSONファイルの構造が正しいか確認

3. **AIチャットが動作しない**
   - APIキーが正しく設定されているか確認
   - インターネット接続を確認
   - APIの利用制限に達していないか確認

4. **過去の問題が表示されない**
   - 日付ボタンをクリックしているか確認
   - 同じ日付を再度クリックすると閉じる仕様

## 📝 今後の予定

- [ ] ユーザーの学習進捗トラッキング機能
- [ ] 問題の正答率表示
- [ ] カテゴリー別問題出題
- [ ] 模擬試験機能
- [ ] 学習リマインダー機能
- [ ] 問題の難易度設定
- [ ] 学習統計の可視化
- [ ] モバイルアプリ版の開発

## 📄 ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## 🤝 貢献

プルリクエストを歓迎します。大きな変更を行う場合は、まずissueを開いて変更内容を議論してください。

### 貢献の方法
1. フォークする
2. フィーチャーブランチを作成する (`git checkout -b feature/AmazingFeature`)
3. 変更をコミットする (`git commit -m 'Add some AmazingFeature'`)
4. ブランチにプッシュする (`git push origin feature/AmazingFeature`)
5. プルリクエストを開く

## 👤 作者

Show Hey AI

## 🔗 リンク

- [ライブサイト](https://show-hey-ai.github.io/bizlaw-site/)
- [問題の報告](https://github.com/show-hey-ai/bizlaw-site/issues)
- [Google Gemini API](https://ai.google.dev/)

---

⭐ このプロジェクトが役に立ったら、スターをお願いします！