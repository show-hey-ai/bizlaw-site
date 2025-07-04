import os
import json
import google.generativeai as genai
from datetime import datetime
import sys

# Google APIキーの設定
api_key = os.environ.get('GOOGLE_API_KEY')
if not api_key:
    print("Error: GOOGLE_API_KEY environment variable not set")
    sys.exit(1)

genai.configure(api_key=api_key)

# モデルの設定
model = genai.GenerativeModel('gemini-pro')

def generate_daily_quote():
    """今日の名言を生成"""
    prompt = """
    ビジネス法務検定の学習者に向けて、努力、目的達成、夢に関する偉人の名言を1つ生成してください。
    
    要件：
    1. 実在の偉人（歴史上の人物、有名な経営者、哲学者など）の名前を含める
    2. その偉人が実際に言いそうな名言にする（完全な創作でも構いませんが、その人物の思想に合致したもの）
    3. 日本語訳と原文（英語やその他の言語）の両方を含める
    4. その名言から学べる教訓を簡潔に説明する
    
    次のJSON形式で回答してください：
    {
        "author": "偉人の名前",
        "quote_ja": "日本語の名言",
        "quote_original": "原文の名言（存在する場合）",
        "lesson": "この名言から学べること（100文字以内）"
    }
    """
    
    try:
        response = model.generate_content(prompt)
        # レスポンスからJSONを抽出
        text = response.text
        # マークダウンのコードブロックを除去
        if '```json' in text:
            text = text.split('```json')[1].split('```')[0]
        elif '```' in text:
            text = text.split('```')[1].split('```')[0]
        
        quote_data = json.loads(text.strip())
        
        # 日付情報を追加
        quote_data['date'] = datetime.now().strftime('%Y-%m-%d')
        
        return quote_data
    except Exception as e:
        print(f"Error generating quote: {e}")
        # エラー時のデフォルト名言
        return {
            "author": "トーマス・エジソン",
            "quote_ja": "天才とは、1％のひらめきと99％の努力である。",
            "quote_original": "Genius is one percent inspiration and ninety-nine percent perspiration.",
            "lesson": "成功は努力の積み重ねから生まれます。毎日の学習を大切にしましょう。",
            "date": datetime.now().strftime('%Y-%m-%d')
        }

def save_quote(quote_data):
    """名言をJSONファイルに保存"""
    date_str = datetime.now().strftime('%Y%m%d')
    filename = f'data/quote_{date_str}.json'
    
    # dataディレクトリが存在しない場合は作成
    os.makedirs('data', exist_ok=True)
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump({'quote': quote_data}, f, ensure_ascii=False, indent=2)
    
    print(f"Quote saved to {filename}")

def main():
    print("Generating daily quote...")
    quote = generate_daily_quote()
    save_quote(quote)
    print("Quote generation completed!")
    print(f"Author: {quote['author']}")
    print(f"Quote: {quote['quote_ja']}")

if __name__ == "__main__":
    main()
