
import os
import google.generativeai as genai

try:
    # 環境変数からAPIキーを取得
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")

    # APIキーを設定
    genai.configure(api_key=api_key)

    # モデルを初期化
    model = genai.GenerativeModel('gemini-pro')

    # 簡単なプロンプトでコンテンツを生成
    response = model.generate_content("This is a test. If you see this, the API is working. Respond with 'OK'.")

    # 応答をチェック
    if "OK" in response.text:
        print("Gemini API setup is successful!")
        print("Response from API:", response.text)
    else:
        print("API call was successful, but the response was not as expected.")
        print("Full response:", response.text)

except Exception as e:
    print(f"An error occurred: {e}")

