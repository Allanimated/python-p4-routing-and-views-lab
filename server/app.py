#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f"{parameter}"


@app.route('/count/<int:parameter>')
def count(parameter):
    markup = ""
    for num in range(parameter):
        markup += f"{num}\n"

    return markup


@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    answer = None
    if operation == "+":
        answer = num1 + num2
    elif operation == "-":
        answer = num1-num2
    elif operation == "*":
        answer = num1*num2
    elif operation == "div":
        answer = num1/num2
    elif operation == "%":
        answer = num1 % num2
    else:
        answer = "Invalid operation"

    return f"{answer}"


if __name__ == '__main__':
    app.run(port=5555, debug=True)
