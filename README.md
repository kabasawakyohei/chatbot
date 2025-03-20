# Flaskチャットボットアプリケーション

このアプリケーションは、FlaskとCohereを使用した簡単なチャットボットです。

## セットアップ手順

1. 必要なパッケージをインストール:
```bash
pip install -r requirements.txt
```

2. `.env`ファイルを作成し、CohereのAPIキーを設定:
```
COHERE_API_KEY=your_api_key_here
```

3. アプリケーションの起動:
```bash
python app.py
```

4. ブラウザで以下のURLにアクセス:
```
http://localhost:5000
```

## 機能
- ユーザーとAIの会話を異なる色で表示
- シンプルで使いやすいインターフェース
- リアルタイムのチャット応答

## 技術スタック
- Flask
- Cohere AI
- HTML/CSS
- JavaScript 