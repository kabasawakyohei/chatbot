from flask import Flask, render_template, request, jsonify
import cohere
import os
from dotenv import load_dotenv

# 環境変数の読み込み（開発環境のみ）
if os.path.exists('.env'):
    load_dotenv()

app = Flask(__name__)

# Cohereクライアントの初期化
co = cohere.Client(os.getenv('COHERE_API_KEY'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    
    # Cohereを使用して応答を生成
    response = co.chat(
        message=user_message,
        temperature=0.7,
        return_chat_history=False
    )
    
    return jsonify({
        'response': response.text
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000))) 