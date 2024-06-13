import os
import openai
from flask import Flask, request, jsonify
from dotenv import load_dotenv

app = Flask(__name__)

# Load OpenAI API key from environment variable
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/api/chatgpt', methods=['POST'])
def chatgpt():
    try:
        data = request.json
        message = data.get('message', '')

        # Call OpenAI API
        response = openai.Completion.create(
            engine="davinci",
            prompt=message,
            max_tokens=50
        )
        reply = response.choices[0].text.strip()

        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
