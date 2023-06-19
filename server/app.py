#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>')
def print_string(text):
    print(text)  
    return text

@app.route('/count/<int:num>')
def count(num):
    if num < 0:
        return 'Invalid parameter.'

    numbers = "\n".join(str(i) for i in range(num + 1))
    return f'<pre>{numbers}</pre>'

@app.route('/math/<float:num1>/<string:operation>/<float:num2>')
def math(num1, operation, num2):
    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
    elif operation == '%':
        result = num1 % num2

    if result is not None:
        return f'{result}'
    else:
        return 'Invalid operation or division by zero.'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
