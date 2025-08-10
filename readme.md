# 🏨 Hotel Booking API (FastAPI)

Простой и функциональный API для бронирования отелей с использованием FastAPI.

## 🔹 Основные возможности
- 🔐 Аутентификация через JWT
- 🏩 Просмотр отелей и номеров
- 📅 Бронирование (создание, просмотр, отмена)
- ⚡ Кэширование через Redis (в разработке)
- 🗃️ Работа с PostgreSQL
- 🐳 Docker-контейнеризация

## 🛠 Стек технологий
- **Backend**: FastAPI (асинхронный), Python 3.10+
- **База данных**: PostgreSQL
- **Кэширование**: Redis + Celery
- **Деплой**: Docker, Docker Compose

## ⚙️ Настройка окружения

1. Создайте файл `.env` на основе примера:
   ```bash
   cp .env.example .env

## 🚀 Запуск проекта  
### Локально (с Docker)  
```bash
docker-compose up --build

Доступные интерфейсы:
- 🔧 Администрирование: [http://localhost:7777/admin](http://localhost:7777/admin)
- 📊 Мониторинг задач: [http://localhost:5555](http://localhost:5555)
- 📚 API документация: [http://localhost:7777/docs](http://localhost:7777/docs)
