 from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/chatgpt', methods=['POST'])
def chatgpt():
    data = request.json
    message = data.get('message', '')
    # Here you would add your logic to interact with ChatGPT
    response = {"reply": f"Received: {message}"}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
