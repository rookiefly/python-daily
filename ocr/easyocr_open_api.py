import os
import time
import easyocr
from flask import Flask, request, jsonify, g

UPLOAD_FOLDER = './upload'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.before_request
def before_request():
    g.request_start_time = time.time()


@app.after_request
def after_request(response):
    g.request_time = lambda: "%.5fs" % (time.time() - g.request_start_time)
    print(g.request_time())
    return response


@app.route('/api/ocr', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file1' not in request.files:
            return 'there is no file1 in form!'
        file1 = request.files['file1']
        path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
        file1.save(path)
        # need to run only once to load model into memory
        reader = easyocr.Reader(['ch_sim', 'en'])
        result = reader.readtext('chinese.jpeg',  detail=0)
        return jsonify(result)

    return '''
    <h1>Upload new File</h1>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="file1">
      <input type="submit">
    </form>
    '''


if __name__ == '__main__':
    app.run()
