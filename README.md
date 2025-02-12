# 📧 Django Email Sender

&#x20; &#x20;

Email Sender — это сервис на Python 2.7 / Django 1.9.9 для отправки email-рассылок с поддержкой HTML-шаблонов, отложенной отправки (через Celery) и отслеживания открытий писем.

## 📌 Возможности

✅ Отправка email-рассылок с HTML-шаблоном и списком подписчиков\
✅ Использование AJAX-запросов для создания рассылки (jQuery, Bootstrap)\
✅ Отложенная отправка писем через Celery\
✅ Поддержка переменных в письмах (имя, фамилия, день рождения)\
✅ Отслеживание открытий писем

---

## 🚀 Запуск без Docker

### 📥 Установка зависимостей

```bash
pip install -r requirements.txt
```

### 🔥 Запуск сервиса

#### 1. Настройка PostgreSQL и Redis (локально или через .env)

#### 2. Применение миграций

```bash
python manage.py migrate
```

#### 3. Запуск Django-сервера

```bash
python manage.py runserver
```

#### 4. Запуск Celery-воркера

```bash
celery -A config worker --loglevel=info
```

---

## 🐳 Запуск через Docker

```bash
docker-compose up --build -d
```

Docker запускает 4 сервиса:

- `db` — PostgreSQL 9.6
- `redis` — брокер для Celery
- `web` — Django-приложение
- `celery` — Celery-воркер для обработки отложенных задач

Применить миграции можно командой:

```bash
docker-compose exec web python manage.py migrate
```

---

## Структура API

| Метод | URL | Описание |
|--------|-------------------|---------------------------------------------|
| `GET` | `/` | Главная страница сервиса рассылок |
| `GET` | `/subscribers` | Страница списка подписчиков |
| `POST` | `/create/` | Создать новую email-рассылку |
| `POST` | `/subscribers/add` | Добавить нового подписчика |
| `GET` | `/subscribers/list` | Получить список подписчиков (JSON) |
| `GET` | `/tracker/?email={email}` | Трекинг открытия email |

---

## ⚙️ Переменные окружения (.env)

```ini
# PostgreSQL
POSTGRES_DB=database_name
POSTGRES_USER=username
POSTGRES_PASSWORD=password
POSTGRES_HOST=postgres_django
POSTGRES_PORT=5432

# Django
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=*

# Email SMTP
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_password
EMAIL_TRACKER_SERVER=https://your-server.com

# Celery
CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0
```

---

## 📜 Лицензия

MIT License © 2025

