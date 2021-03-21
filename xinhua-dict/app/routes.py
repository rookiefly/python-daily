from app import app
from flask import Response, request
import json
import jsonpath


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/dictionary')
def searchDict():
    key = request.args.get('key')
    with open('./data/word.json', 'r') as jsonFile:
        wordDict = json.load(jsonFile)
        return Response(json.dumps(jsonpath.jsonpath(wordDict, "$.[?(@.word=='" + key + "')]")), mimetype='application/json')


@app.route('/json')
def jsonTest():
    t = {
        'a': 1,
        'b': 2,
        'c': [3, 4, 5]
    }
    return Response(json.dumps(t), mimetype='application/json')
