from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='client', static_folder='client/src')
app.secret_key = 'LN$oaYB9-5KBT7G'

@app.route("/")
def main():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')