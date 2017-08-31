# from flask import Flask
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
# if __name__ == '__main__':
#     app.run()

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/mtcnn', methods=['POST','GET'])
def getLocation():
    if request.method == 'POST':
        return request.form['img_data']



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8888, debug=True)
