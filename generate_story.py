#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ビジ法3級合格体験談生成スクリプト
Google Gemini APIを使用してモチベーション向上のための体験談を生成し、JSONファイルとして保存する
"""

import os
import json
import google.generativeai as genai
from datetime import datetime
import sys

def generate_story():
    """
    Google Gemini APIを使用してビジ法3級合格体験談を生成
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
ビジネス法務検定3級に合格した人の体験談を1つ作成してください。
以下の形式のJSONで回答してください：

{
  "story": {
    "content": "体験談の内容（150文字程度）",
    "tone": "motivational",
    "themes": ["継続", "努力", "成長"]
  },
  "generated_date": "2024-12-29"
}

要件：
- 150文字程度で簡潔にまとめる
- 学習者のモチベーション向上に繋がる内容
- リアルで共感しやすいエピソード
- 前向きで励ましになるトーン
- 具体的な学習方法や期間を含める
- 挫折を乗り越えた話や、継続の大切さを伝える
- 毎回異なるパターンの体験談にする

必ずJSONのみを返し、説明文は不要です。
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
        story_data = json.loads(json_content)
        
        # 生成日時を現在の日付に設定
        story_data['generated_date'] = datetime.now().strftime('%Y-%m-%d')
        
        return story_data
        
    except json.JSONDecodeError as e:
        print(f"JSON解析エラー: {e}")
        print(f"受信データ: {content}")
        return None
    except Exception as e:
        print(f"体験談生成エラー: {e}")
        return None

def save_story_to_file(story_data):
    """
    生成された体験談をJSONファイルに保存
    """
    if not story_data:
        return False
    
    # ファイル名を現在の日付で作成
    today = datetime.now().strftime('%Y%m%d')
    filename = f"data/story_{today}.json"
    
    # dataディレクトリが存在しない場合は作成
    os.makedirs('data', exist_ok=True)
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(story_data, f, ensure_ascii=False, indent=2)
        
        print(f"体験談ファイルを保存しました: {filename}")
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
    print("ビジ法3級体験談生成スクリプト開始（Google Gemini API版）")
    print(f"実行時刻: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    # API キー確認
    if not validate_api_key():
        sys.exit(1)
    
    # 体験談生成
    print("体験談を生成中...")
    story_data = generate_story()
    
    if not story_data:
        print("体験談生成に失敗しました")
        sys.exit(1)
    
    # ファイル保存
    if save_story_to_file(story_data):
        print("体験談生成が正常に完了しました")
        print(f"体験談内容: {story_data.get('story', {}).get('content', 'なし')[:50]}...")
    else:
        print("ファイル保存に失敗しました")
        sys.exit(1)

if __name__ == "__main__":
    main()
