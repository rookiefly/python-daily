from app import app
from flask import Response, request
import json
import jsonpath
from os.path import dirname, abspath, join


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/dict')
def searchDict():
    word = request.args.get('word')
    script_dir = dirname(dirname(abspath(__file__)))
    with open(join(script_dir, "data/word.json"), 'r') as jsonFile:
        wordDict = json.load(jsonFile)
        wordResult = jsonpath.jsonpath(wordDict, "$.[?(@.word=='" + word + "')]")
        return Response(json.dumps(wordResult, ensure_ascii=False), mimetype='application/json')


@app.route('/json')
def jsonTest():
    t = {
        'a': 1,
        'b': 2,
        'c': [3, 4, 5]
    }
    return Response(json.dumps(t), mimetype='application/json')
