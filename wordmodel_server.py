from flask import Flask
from flask import request
from flask import jsonify
from wordmodel import Model
app = Flask(__name__)

model = Model()


@app.route("/", methods=['POST'])
def hello():
    sentence = request.form['sentence']
    return jsonify({'vec': list(model.sentence_vector(sentence))})

if __name__ == "__main__":
    app.run(port=8888)
