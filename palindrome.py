import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/palindrome', methods=['POST'])
def palindrome():
    content = request.json
    print(content['data'])
    data = content["data"]
    results = []
    if len(data)==0:
        return jsonify({"Status":"Array cannot be empty"})
    for idx,value in enumerate(data):
        if value and value==value[::-1]:
            results.append(idx)
    if len(results)==0:
        return jsonify({"Status":"No Palindrome found"})
    return jsonify({"Palindrome string @indexes":results})

app.run()

