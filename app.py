# coding=utf8
from flask import Flask, render_template, request

app = Flask(__name__)

def stringify(user_number, factors):
  """ Формирование строки в виде уравнения из исходного значения и множителей. """
  return str(user_number) + ' = ' + ' * '.join(map(str, factors))


def factorize(n):
  """ Факторизация числа методом перебора делителей. """
  if n <= 0:
    return ('Это не натуральное число :(').decode('utf-8')
  elif n == 1:
    return ('Это число не раскладывается на множители').decode('utf-8')
  else:
    user_number = n
    factors = []
    i = 2
    while i * i <= n:         # Диапазон поиска делителей от 2 до n^1/2
      while n % i == 0:
        factors.append(i)     
        n = n / i             
      i += 1
    if n > 1:
      factors.append(n)
    if n == user_number:
      return str(user_number) + ' - простое число'.decode('utf-8')    # n не изменилось -> простое число
    else:
      return stringify(user_number, factors)


@app.route("/", methods=['POST', 'GET'])
def main():
  answer = None  
  if request.method == 'POST':
    data = request.form['input_number']    # Если вызван метод POST, получить данные из поля формы
    if data:
      user_number = int(data)              # Если получена не пустая строка, преобразовать ее в число     
      answer = factorize(user_number)      # и выполнить факторизацию

  return render_template('index.html', answer = answer)

if __name__ == "__main__":
    app.run()