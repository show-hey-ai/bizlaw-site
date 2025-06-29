#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ビジ法3級問題生成スクリプト
Google Gemini APIを使用して日々の○×問題を生成し、JSONファイルとして保存する
"""

import os
import json
import google.generativeai as genai
from datetime import datetime
import sys

def generate_questions():
    """
    Google Gemini APIを使用してビジ法3級の○×問題10問を生成
    """
    # APIキーを環境変数から取得
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        print("エラー: GOOGLE_API_KEY環境変数が設定されていません")
        return None
    
    # Gemini APIを設定
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
    
    prompt = """
ビジネス法務検定3級レベルの○×問題を10問作成してください。
以下の形式のJSONで回答してください：

{
  "questions": [
    {
      "id": 1,
      "question": "問題文",
      "answer": true,
      "explanation": "解説文"
    },
    {
      "id": 2,
      "question": "問題文",
      "answer": false,
      "explanation": "解説文"
    }
  ],
  "generated_date": "2024-12-29",
  "topic_areas": ["契約法", "会社法", "知的財産権", "労働法", "個人情報保護法"]
}

要件：
- 問題は具体的で実務に役立つ内容にする
- 解説は150文字程度で簡潔に
- 答えはtrue（○）またはfalse（×）のboolean値
- 契約法、会社法、知的財産権、労働法、個人情報保護法などの分野をバランスよく含める
- 最新の法改正も考慮する
- 問題の難易度は3級レベル（基本的な知識）に合わせる
- 必ずJSONのみを返し、説明文は不要です
"""

    try:
        response = model.generate_content(prompt)
        content = response.text.strip()
        
        # JSONの開始と終了を見つける
        start = content.find('{')
        end = content.rfind('}') + 1
        
        if start == -1 or end == 0:
            print(f"有効なJSONが見つかりません。出力: {content}")
            return None
            
        json_content = content[start:end]
        questions_data = json.loads(json_content)
        
        # 生成日時を現在の日付に設定
        questions_data['generated_date'] = datetime.now().strftime('%Y-%m-%d')
        
        return questions_data
        
    except json.JSONDecodeError as e:
        print(f"JSON解析エラー: {e}")
        print(f"受信データ: {content}")
        return None
    except Exception as e:
        print(f"問題生成エラー: {e}")
        return None

def save_questions_to_file(questions_data):
    """
    生成された問題をJSONファイルに保存
    """
    if not questions_data:
        return False
    
    # ファイル名を現在の日付で作成
    today = datetime.now().strftime('%Y%m%d')
    filename = f"data/questions_{today}.json"
    
    # dataディレクトリが存在しない場合は作成
    os.makedirs('data', exist_ok=True)
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(questions_data, f, ensure_ascii=False, indent=2)
        
        print(f"問題ファイルを保存しました: {filename}")
        return True
        
    except Exception as e:
        print(f"ファイル保存エラー: {e}")
        return False

def validate_api_key():
    """
    Google API キーの有効性を確認
    """
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        print("エラー: GOOGLE_API_KEY環境変数が設定されていません")
        print("設定方法:")
        print('setx GOOGLE_API_KEY "your-api-key-here"')
        return False
    
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.0-flash-exp')
        # 簡単なテスト
        response = model.generate_content("こんにちは")
        print("Google Gemini API接続確認完了")
        return True
    except Exception as e:
        print(f"Google Gemini API接続エラー: {e}")
        return False

def main():
    """
    メイン実行関数
    """
    print("=" * 50)
    print("ビジ法3級問題生成スクリプト開始（Google Gemini API版）")
    print(f"実行時刻: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    # API キー確認
    if not validate_api_key():
        sys.exit(1)
    
    # 問題生成
    print("問題を生成中...")
    questions_data = generate_questions()
    
    if not questions_data:
        print("問題生成に失敗しました")
        sys.exit(1)
    
    # ファイル保存
    if save_questions_to_file(questions_data):
        print("問題生成が正常に完了しました")
        print(f"生成された問題数: {len(questions_data.get('questions', []))}")
    else:
        print("ファイル保存に失敗しました")
        sys.exit(1)

if __name__ == "__main__":
    main()
