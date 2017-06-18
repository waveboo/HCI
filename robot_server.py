# encoding=utf-8

from flask import Flask
from flask import request
#from flask import jsonify
from robot import Robot


app = Flask(__name__)


@app.route("/ask", methods=['POST'])
def ask():
    """

     accept type: json
     accept format: json
     {
        "question": xxx
        ...
     }

     return type : json
     return format:
        {
            "instructions": {
                "say": xxx,
                "move": xxx,
                ...
            }
        }

    """
    robot = Robot()
    # data = request.json
    question = request.form['question']
    print question
    answer = robot.listen(question)
    print answer
    # resp = {
    #     'instructions': {
    #         'say': answer
    #     }
    # }
    return answer

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
