Та самая Россия 
# Инструкция по установке и запуску проекта

### 1. Клонирование репозитория
git clone https://github.com/your-username/that-very-russia.git
cd that-very-russia/backend

### 2. Создание виртуального окружения
### Linux / MacOS:
python3 -m venv venv
source venv/bin/activate

#### Windows:
python -m venv venv
venv\Scripts\activate

### 3. Установка зависимостей
pip install -r requirements.txt

### 4. Применение миграций
python manage.py migrate

### 5. (Опционально) создание суперпользователя
python manage.py createsuperuser

### 6. Запуск сервера разработки
python manage.py runserver
Проект будет доступен по адресу: http://127.0.0.1:8000/


### Структура проекта
 backend/
 ├── manage.py
 ├── db.sqlite3
 ├── backend/
 │   ├── asgi.py
 │   ├── settings.py
 │   ├── urls.py
 │   └── wsgi.py
 ├── core/
 │   ├── admin.py
 │   ├── apps.py
 │   ├── models.py
 │   ├── views.py
 │   ├── migrations/
 │   ├── static/
 │   │   ├── css/
 │   │   ├── img/
 │   │   └── js/
 │   └── templates/
 └── media/
     ├── history/
     ├── history_line/
     ├── news/
     ├── news_images/
     ├── organizers/
     ├── partners/
     └── team_images/
