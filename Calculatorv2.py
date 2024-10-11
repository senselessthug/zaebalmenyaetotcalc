from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    import os
    print(os.access('templates/index.html', os.R_OK))  # Проверка прав на чтение
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    operation = request.form['operation']
    num2 = float(request.form['num2'])

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Ділення на нуль неможливе"
    else:
        result = "Невідома операція"

    return render_template('tasks.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
