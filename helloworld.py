import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/hello-world', methods=['GET'])
def home():
    return "HELLO WORLD"

app.run()