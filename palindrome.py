import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

count=0
@app.route('/hello-world', methods=['GET'])
def home():
    return "HELLO WORLD"

@app.route('/get-count', methods=['GET'])
def getCount():
    return "Total number of times /check palindrome api is called:"+str(count)

@app.route('/palindrome', methods=['POST'])
def palindrome():
    global count
    count=count+1
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

