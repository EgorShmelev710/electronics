# Electronics

## Описание

Сеть по продаже электронкики.

## Задание
- Создайте веб-приложение с API-интерфейсом и админ-панелью.
- Создайте базу данных, используя миграции Django.

## Технологии

- Python
- Django
- DRF
- PostgreSQL


## Настройка проекта

### Клонирование проекта

Для работы с проектом клонируйте репозиторий

  ```sh
  git clone git@github.com:EgorShmelev710/electronics.git
  ```

### Настройка виртуального окружения

Создайте виртуальное окружение командой:

```text
python3 -m venv venv
```

Активируйте виртуальное окружение:

```text
source venv/bin/activate          # для Linux и Mac
venv\Scripts\activate         # для Windows
```

Устанавите зависимости командой:

```text
pip install -r requirements.txt
```

### Редактирование .env.sample:

- В корне проекта переименуйте файл .env.sample в .env и отредактируйте параметры:
    ```text
    SECRET_KEY=секрктный ключ django
    
    NAME=название базы данных
    USER=пользователь базы данных
    PASSWORD=ваш пароль
    HOST=хост базы данных
    PORT=порт
    
    TIME_ZONE=ваш часовой пояс
    
    DEBUG=False (установить по желанию)
    ```

### Настройка БД и кэширования:

- Создайте миграции:
  ```text
  python manage.py makemigrations
  ```

- Примените миграции:
  ```text
  python manage.py migrate
  ```
  


## Использование


- Для запуска проекта наберите в терминале команду:
  ```text
  python manage.py runserver
  ```
  Админ-панель доступна после запуска проекта по адресу: http://localhost:8000/admin/

## Документация
 Документация доступна после запуска проекта по адресу: http://localhost:8000/swagger/ или http://localhost:8000/redoc/ 
## Контакты

Ссылка на репозиторий: [https://github.com/EgorShmelev710](https://github.com/EgorShmelev710)



