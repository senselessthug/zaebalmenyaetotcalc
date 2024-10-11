from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    import os
    print(os.access('templates/index.html', os.R_OK))  # Проверка прав на чтение
    return render_template('index.html')


@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
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
                result = "Деление на ноль невозможно"
        else:
            result = "Неизвестная операция"

        return render_template('tasks.html', result=result)
    else:
        return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
