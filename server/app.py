#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
  
@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:text>')
def print_string(text):
    print(text)  # This will print the string to the console
    return f"<p>Printed: {text}</p>"

@app.route('/count/<int:num>')
def count(num):
    numbers = '\n'.join(map(str, range(1, num + 1)))
    return f"<pre>{numbers}</pre>"

@app.route('/math/<int:num1><string:operation><int:num2>')
def math(num1, operation, num2):
    result = 0
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Division by zero is not allowed."
    elif operation == '%':
        if num2 != 0:
            result = num1 % num2
        else:
            return "Modulus by zero is not allowed."

    return f"<p>{num1} {operation} {num2} = {result}</p>"
