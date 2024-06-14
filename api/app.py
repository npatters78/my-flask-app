import os
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Log Flask version
import flask
print(f"Flask version: {flask.__version__}")

# Additional logging for deployment trigger
print("Deployment triggered")

# Retrieve the API key from the environment variable
openai_api_key = os.getenv('OPENAI_API_KEY')
if openai_api_key is None:
    raise ValueError("No OpenAI API key found in environment variables.")
openai.api_key = openai_api_key

@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json.get('input')
    if user_input is None:
        return jsonify({"error": "No input provided"}), 400

    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=user_input,
            max_tokens=150
        )
        return jsonify(response.choices[0].text.strip())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/version', methods=['GET'])
def version():
    return jsonify({"flask_version": flask.__version__})

if __name__ == '__main__':
    app.run()
# Minor change to trigger redeployment again
