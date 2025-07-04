#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
過去の日付の体験談を生成するスクリプト
"""

import os
import sys
import json
from datetime import datetime, timedelta

# 親ディレクトリをパスに追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.generate_story import generate_story

def generate_past_story(days_ago):
    """指定された日数前の体験談を生成"""
    # 体験談を生成
    story_data = generate_story()
    
    if not story_data:
        print(f"体験談生成に失敗しました")
        return False
    
    # 日付を過去に設定
    past_date = datetime.now() - timedelta(days=days_ago)
    date_str = past_date.strftime('%Y%m%d')
    
    story_data['generated_date'] = past_date.strftime('%Y-%m-%d')
    
    # ファイル保存
    filename = f"data/story_{date_str}.json"
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(story_data, f, ensure_ascii=False, indent=2)
        
        print(f"過去の体験談ファイルを保存しました: {filename}")
        return True
        
    except Exception as e:
        print(f"ファイル保存エラー: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使用方法: python generate_past_story.py [何日前]")
        print("例: python generate_past_story.py 3")
        sys.exit(1)
    
    days_ago = int(sys.argv[1])
    
    print(f"{days_ago}日前の体験談を生成します...")
    if generate_past_story(days_ago):
        print("生成完了！")
    else:
        print("生成失敗")
