import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/api/chatgpt', methods=['POST'])
def chatgpt():
    try:
        data = request.json
        app.logger.info(f"Received data: {data}")
        message = data.get('message', '')
        response = {"reply": f"Received: {message}"}
        app.logger.info(f"Response: {response}")
        return jsonify(response)
    except Exception as e:
        app.logger.error(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
