from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def root():
    return 'W'


@app.route('/predict', methods=['GET'])
def predict():
    return 'p'


app.run(port=9090, debug=True)
