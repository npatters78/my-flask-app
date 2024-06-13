from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/chatgpt', methods=['POST'])
def chatgpt():
    try:
        data = request.json
        message = data.get('message', '')
        response = {"reply": f"Received: {message}"}
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()