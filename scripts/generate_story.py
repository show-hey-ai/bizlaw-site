#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ビジ法3級合格体験談生成スクリプト（高ランダム性版）
Google Gemini APIを使用して多彩なバリエーションの体験談を生成し、JSONファイルとして保存する
"""

import os
import json
import google.generativeai as genai
from datetime import datetime
import sys
import random

def generate_story():
    """
    Google Gemini APIを使用してビジ法3級合格体験談を生成（高ランダム性）
    """
    # APIキーを環境変数から取得
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        print("エラー: GOOGLE_API_KEY環境変数が設定されていません")
        return None
    
    # Gemini APIを設定
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
    
    # ランダムな体験談パターンを定義
    story_patterns = [
        # パターン1: 初心者から合格まで
        {
            "persona": "法律知識ゼロの完全初心者",
            "occupation": "IT系会社員",
            "study_method": "過去問中心の勉強法",
            "tone": "親しみやすい関西弁",
            "length": "120-150字",
            "emotion": "最初は不安だったけど"
        },
        # パターン2: 働きながら合格
        {
            "persona": "忙しい営業マン",
            "occupation": "商社勤務",
            "study_method": "電車の中でのスキマ時間学習",
            "tone": "丁寧語でビジネスライク",
            "length": "130-160字",
            "emotion": "時間がなくて焦ったけど"
        },
        # パターン3: 学生の合格体験
        {
            "persona": "大学3年生",
            "occupation": "経済学部学生",
            "study_method": "友達と一緒にグループ学習",
            "tone": "若者らしい元気な口調",
            "length": "100-130字",
            "emotion": "友達と競い合って楽しかった"
        },
        # パターン4: 主婦の合格体験
        {
            "persona": "子育て中の主婦",
            "occupation": "パートタイム勤務",
            "study_method": "育児の合間にコツコツ勉強",
            "tone": "温かみのある女性らしい口調",
            "length": "140-170字",
            "emotion": "子どもが寝た後の時間が貴重で"
        },
        # パターン5: シニアの合格体験
        {
            "persona": "50代のシニア",
            "occupation": "中小企業の総務課長",
            "study_method": "じっくり基礎から体系的学習",
            "tone": "落ち着いた大人の口調",
            "length": "150-180字",
            "emotion": "年齢的に不安だったが"
        },
        # パターン6: 再挑戦での合格
        {
            "persona": "一度失敗した再挑戦者",
            "occupation": "経理担当者",
            "study_method": "前回の失敗を分析した弱点克服学習",
            "tone": "力強い励ましの口調",
            "length": "120-150字",
            "emotion": "一度落ちて悔しかったけど"
        },
        # パターン7: 短期集中合格
        {
            "persona": "1ヶ月で合格を目指した人",
            "occupation": "フリーランス",
            "study_method": "超集中的な1日8時間学習",
            "tone": "エネルギッシュな口調",
            "length": "110-140字",
            "emotion": "短期間で無謀だと思ったけど"
        },
        # パターン8: 独学での合格
        {
            "persona": "完全独学者",
            "occupation": "システムエンジニア",
            "study_method": "書籍とネットを駆使した独自学習法",
            "tone": "クールで知的な口調",
            "length": "130-160字",
            "emotion": "誰にも頼らず一人で挑戦"
        },
        # パターン9: 文系から挑戦
        {
            "persona": "文学部出身の文系人間",
            "occupation": "出版社勤務",
            "study_method": "法律用語の暗記から始めた基礎固め",
            "tone": "知的で上品な口調",
            "length": "140-170字",
            "emotion": "法律は全くの専門外で"
        },
        # パターン10: アルバイト学生
        {
            "persona": "アルバイトしながらの学生",
            "occupation": "大学生（アルバイト多忙）",
            "study_method": "バイトの休憩時間を活用した細切れ学習",
            "tone": "カジュアルで親近感のある口調",
            "length": "120-150字",
            "emotion": "バイトが忙しくて大変だったけど"
        }
    ]
    
    # ランダムな要素を定義
    study_periods = ["1ヶ月", "2ヶ月", "3ヶ月", "4ヶ月", "半年間", "3週間", "2週間"]
    
    difficulties = [
        "法律用語が難しくて", "範囲が広すぎて", "時間管理が大変で", 
        "集中力が続かなくて", "理解が追いつかなくて", "暗記が苦手で",
        "計算問題でつまずいて", "条文の読み方が分からなくて"
    ]
    
    success_factors = [
        "継続は力なり", "毎日少しずつが大切", "諦めないことが一番", 
        "基礎をしっかり固めること", "過去問の反復が効果的", "仲間との励まし合い",
        "自分のペースを見つけること", "苦手分野の重点克服", "計画的な学習スケジュール"
    ]
    
    motivational_phrases = [
        "絶対に諦めないで", "きっとできるから頑張って", "一歩ずつ前進すれば大丈夫",
        "失敗を恐れずチャレンジ", "自分を信じて最後まで", "小さな積み重ねが大きな成果に",
        "努力は必ず報われる", "今日の頑張りが明日の自信に"
    ]
    
    study_tools = [
        "市販のテキスト", "過去問題集", "オンライン講座", "YouTube動画",
        "スマホアプリ", "図書館の参考書", "友人からの借り物", "無料のWebサイト"
    ]
    
    # ランダムに要素を選択
    selected_pattern = random.choice(story_patterns)
    selected_period = random.choice(study_periods)
    selected_difficulty = random.choice(difficulties)
    selected_success = random.choice(success_factors)
    selected_motivation = random.choice(motivational_phrases)
    selected_tool = random.choice(study_tools)
    
    # 季節やタイミングもランダム化
    study_timing = random.choice([
        "春から勉強を始めて", "夏休みを利用して", "秋の試験に向けて", 
        "年末年始の休暇中に", "新年度の目標として", "転職を機に"
    ])
    
    # より詳細で多様なプロンプトを作成
    prompt = f"""
ビジネス法務検定3級に合格した人の体験談を1つ作成してください。
以下の形式のJSONで回答してください：

{{
  "story": {{
    "content": "体験談の内容（{selected_pattern['length']}）",
    "tone": "{selected_pattern['tone']}",
    "themes": ["継続", "努力", "成長"]
  }},
  "generated_date": "2024-12-29"
}}

詳細設定：
【人物設定】
- 人物: {selected_pattern['persona']}
- 職業: {selected_pattern['occupation']}
- 文体・口調: {selected_pattern['tone']}
- 文字数: {selected_pattern['length']}

【学習背景】
- 開始のきっかけ: {study_timing}
- 勉強期間: {selected_period}
- 主な学習方法: {selected_pattern['study_method']}
- 使用教材: {selected_tool}

【体験の要素】
- 感情・心境: {selected_pattern['emotion']}
- 困難だった点: {selected_difficulty}
- 成功の秘訣: {selected_success}
- 後輩へのメッセージ: {selected_motivation}

【体験談の要件】
- 指定された文字数内で簡潔にまとめる
- リアルで共感しやすい具体的なエピソード
- その人らしい自然な口調で書く
- 学習者のやる気を引き出す前向きな内容
- 挫折や困難も含めた等身大の体験
- 実践的で参考になるアドバイス
- 毎回全く異なる表現や体験を使う
- 設定された人物像に合った自然な語りかけ

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
        
        # 生成日時と選択されたパターン情報を追加
        story_data['generated_date'] = datetime.now().strftime('%Y-%m-%d')
        story_data['pattern_info'] = {
            'persona': selected_pattern['persona'],
            'occupation': selected_pattern['occupation'],
            'tone': selected_pattern['tone'],
            'study_period': selected_period,
            'difficulty': selected_difficulty,
            'success_factor': selected_success
        }
        
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
    print("ビジ法3級体験談生成スクリプト開始（高ランダム性版）")
    print(f"実行時刻: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    # API キー確認
    if not validate_api_key():
        sys.exit(1)
    
    # 体験談生成
    print("多彩なバリエーションの体験談を生成中...")
    story_data = generate_story()
    
    if not story_data:
        print("体験談生成に失敗しました")
        sys.exit(1)
    
    # 生成された体験談のパターン情報を表示
    pattern_info = story_data.get('pattern_info', {})
    print(f"選択されたパターン: {pattern_info.get('persona', '不明')} ({pattern_info.get('tone', '不明')})")
    print(f"勉強期間: {pattern_info.get('study_period', '不明')}")
    
    # ファイル保存
    if save_story_to_file(story_data):
        print("体験談生成が正常に完了しました")
        print(f"体験談内容: {story_data.get('story', {}).get('content', 'なし')[:50]}...")
    else:
        print("ファイル保存に失敗しました")
        sys.exit(1)

if __name__ == "__main__":
    main()
