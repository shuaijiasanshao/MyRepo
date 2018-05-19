from flask import Flask, render_template
import time
import random
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('mline.html')


@app.route('/data')
def data():
    curr_time = int(round(time.time() * 1000))
    arr = dict()
    arr.setdefault('data_1', [[curr_time, random.randint(0, 10)]])
    arr.setdefault('data_2', [[curr_time, random.randint(0, 10)]])
    arr.setdefault('data_3', [[curr_time, random.randint(0, 10)]])
    return json.dumps(arr)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=True)
