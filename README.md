### Клиент-серверное приложение для разложения чисел на простые множители.

Клонируйте репозиторий и перейдите в директорию приложения
  ```
  git clone git@github.com:gorobchenkoann/factorization.git

  cd factorization
  ```

Создайте виртуальное окружение, чтобы изолировать приложение и зависимости от системы
  ```
  sudo pip install virtualenv
  
  sudo virtualenv venv
  ```

Активируйте виртуальное окружение
  ```
  source venv/bin/activate
  ```

Установите Flask в виртуальное окружение
  ```
  sudo pip install Flask
  ```

Запустите приложение
  ```
  python app.py
  ```

Приложение доступно в браузере по адресу 

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

![Интерфейс](https://github.com/gorobchenkoann/factorization/blob/master/window.png)
