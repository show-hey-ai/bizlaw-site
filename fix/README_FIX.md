# Bizlaw Site 自動更新修正手順

## 問題の概要
2025年7月3日からGoogle Gemini APIキーが期限切れになり、自動更新が停止していました。

## 実施した修正内容（2025年7月4日）

### 1. APIキーの更新
- 新しいGoogle Gemini APIキーを環境変数に設定
- **重要**: 公開されたAPIキーは即座に無効化し、新しいキーを生成すること

### 2. バッチファイルの改善
- `generate_and_push.bat` を `generate_and_push_fixed.bat` に置き換え
- 主な改善点：
  - APIキーの存在チェック機能を追加
  - エラーハンドリングの強化
  - ログ出力の詳細化
  - データファイル生成確認の追加

### 3. 欠落データの生成
以下の日付のデータを生成・追加：
- 2025年6月30日
- 2025年7月2日
- 2025年7月3日
- 2025年7月4日

### 4. 重複問題の発見
全60問（6日分）を分析した結果、以下の重複を発見：
- 「特許権の存続期間は、特許出願日から20年である。」（3回重複）
- 「著作権は、著作物を創作した時点で自動的に発生し、登録は不要である。」（3回重複）
- 「試用期間中の従業員は、本採用後の従業員よりも解雇が容易である。」（2回重複）

## 修正手順

### 1. 新しいGoogle Gemini APIキーの取得と設定

1. **Google AI Studioにアクセス**
   - https://aistudio.google.com/app/apikey にアクセス
   - Googleアカウントでログイン

2. **新しいAPIキーを作成**
   - 「Create API key」をクリック
   - プロジェクトを選択（または新規作成）
   - 生成されたAPIキーをコピー

3. **APIキーを環境変数に設定**
   ```
   fix\setup_api_key.bat
   ```
   を実行し、コピーしたAPIキーを貼り付ける

### 2. 手動テストの実行

APIキーが正しく設定されたか確認：
```
fix\test_manual_update.bat
```

このスクリプトは：
- APIキーの設定を確認
- 問題と体験談の生成をテスト
- 生成されたファイルを表示

### 3. 過去のデータを補填（オプション）

過去5日分のデータを生成する場合：
```
fix\generate_past_data_batch.bat
```

個別に過去のデータを生成する場合：
```
cd C:\Users\user\Desktop\bizlaw-site
venv\Scripts\activate
python fix\generate_past_questions.py 3  # 3日前のデータ
python fix\generate_past_story.py 3      # 3日前のデータ
```

### 4. 修正版の自動更新スクリプトに置き換え

1. 元のスクリプトをバックアップ（完了済み）：
   ```
   copy generate_and_push.bat generate_and_push_backup.bat
   ```

2. 修正版に置き換え（完了済み）：
   ```
   copy generate_and_push_fixed.bat generate_and_push.bat
   ```

### 5. GitHubへのプッシュ

生成されたファイルをGitHubにプッシュ：
```
cd C:\Users\user\Desktop\bizlaw-site
git add data/*.json
git commit -m "Add missing data and fix duplicates"
git push origin main
```

### 6. Windows タスクスケジューラの確認

タスクスケジューラで自動実行が設定されているか確認：
1. Windowsキー + R → `taskschd.msc` を実行
2. 「Bizlaw Site Auto Update」タスクを探す
3. 実行時刻が毎日6:00 AMになっているか確認
4. 「最終実行結果」でエラーがないか確認

## トラブルシューティング

### APIキーエラーが続く場合
- 環境変数が正しく設定されているか確認：`echo %GOOGLE_API_KEY%`
- 新しいコマンドプロンプトで実行しているか確認
- APIキーにスペースが含まれていないか確認

### Gitプッシュエラーの場合
- GitHub認証情報を確認：`git config --list`
- Personal Access Tokenの期限を確認
- 必要に応じて再認証：`git push origin main` （認証プロンプトが表示される）

### ファイルが生成されない場合
- update_log.txt を確認してエラー詳細を確認
- Python仮想環境が正しくアクティベートされているか確認
- 必要なパッケージがインストールされているか確認

## 今後の改善提案

### 1. 重複チェック機能の追加
- 問題生成時に過去の問題と重複しないようにチェック
- 類似度チェックの実装

### 2. APIキー期限監視
- APIキーの有効期限を定期的にチェックする機能を追加
- 期限切れ前のアラート通知

### 3. エラー通知
- 更新エラー時にメール通知を送る機能を追加
- Slackやその他のチャネルへの通知

### 4. バックアップ機能
- 生成されたデータの定期バックアップ
- 過去データのアーカイブ

### 5. ヘルスチェック
- サイトの正常動作を確認するスクリプトを追加
- データの整合性チェック

## ファイル構造
```
bizlaw-site/
├── generate_and_push.bat        # メインの自動更新スクリプト（修正版に置き換え済み）
├── generate_and_push_backup.bat # オリジナル版のバックアップ
├── data/                        # 生成されたJSONファイルの保存先
│   ├── questions_YYYYMMDD.json  # 各日の問題（10問）
│   └── story_YYYYMMDD.json      # 各日の体験談
├── scripts/                     # Python生成スクリプト
│   ├── generate_questions.py    # 問題生成スクリプト
│   └── generate_story.py        # 体験談生成スクリプト
├── fix/                         # 修正用スクリプト
│   ├── README_FIX.md           # この修正手順書
│   ├── setup_api_key.bat       # APIキー設定
│   ├── test_manual_update.bat  # 手動テスト
│   ├── generate_past_data_batch.bat # 過去データ一括生成
│   ├── generate_past_questions.py   # 過去問題生成
│   └── generate_past_story.py       # 過去体験談生成
├── index.html                  # メインのWebページ
└── update_log.txt              # 更新ログ
```

## 完了状態（2025年7月4日時点）
- ✅ 修正版バッチファイルへの置き換え完了
- ✅ APIキーの設定完了（要更新）
- ✅ 欠落データの生成完了（6/30, 7/2, 7/3, 7/4）
- ✅ GitHubへのプッシュ完了
- ⚠️ 重複問題の修正が必要（7組の重複を発見）
