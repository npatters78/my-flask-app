import os
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Retrieve the API key from the environment variable
openai_api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = openai_api_key

@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json.get('input')
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_input,
        max_tokens=150
    )
    return jsonify(response.choices[0].text.strip())

if __name__ == '__main__':
    app.run()
