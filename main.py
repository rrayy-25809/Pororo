from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, send
import logging
from llm import Model

app = Flask(__name__, template_folder='client', static_folder='client/src')
app.secret_key = 'LN$oaYB9-5KBT7G'
app.logger.setLevel(logging.INFO)
LLM = Model()
socket_io = SocketIO(app)
logger = app.logger
LLM.load_file("")

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/chat", methods=['POST'])
def chat():
    message = request.form.get("message")
    logger.info(message)

    answer = LLM.ask(message)

    return jsonify({"response": answer})

# 테스트 용 웹 소켓 예제, 사용 안 할듯
@socket_io.on("message")
def request_sck(message):
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