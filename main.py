from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, send
import logging

app = Flask(__name__, template_folder='client', static_folder='client/src')
app.secret_key = 'LN$oaYB9-5KBT7G'
app.logger.setLevel(logging.INFO)
socket_io = SocketIO(app)
logger = app.logger

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/chat", methods=['POST'])
def chat():
    message = request.form["message"]
    logger.info(message)

    return jsonify({"response": "This is a simulated response from your LLM."})

@socket_io.on("message")
def request_sck(message): # 웹소켓 예시: 채팅 프로그램
    logger.info(f"message: {message}")
    to_client = {} # 클라이언트에게 보낼 데이터

    if message == 'new_connect':
        to_client['message'] = "새로운 유저가 난입하였다!!"
        to_client['type'] = 'connect'
    else:
        to_client['message'] = message
        to_client['type'] = 'normal'

    # 모든 클라이언트에게 전송
    send(to_client, broadcast=True) # type: ignore

if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0')
    socket_io.run(app, debug=True, port=80, host='0.0.0.0')