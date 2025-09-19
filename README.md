## Тестовое задание##

Приложение на **FastAPI** и **PostgreSQL**.

## Эндпоинты
- `POST /clients/` — создать клиента в бд
- `GET /clients/` — получить полный список клиентов 
- `GET /clients/{client_id}` — получить клиента по ID
- `PUT /clients/{client_id}` — обновить дату окончания подписки клиента
- `DELETE /clients/{client_id}` — удалить клиента

Адрес документации Swagger:  
http://localhost:8000/docs

---

## Установка и запуск

### 1. Клонировать репозиторий и перейти в корень проекта на сервере
```bash
git clone https:https://github.com/nikkes174/TZProject
cd TZProject
```
### 2. Создать .env файл в корне  проекта и указать свои данные для доступа к БД
POSTGRES_USER= 'ПГ логин'
POSTGRES_PASSWORD= ПГ пароль
POSTGRES_DB= Название БД
POSTGRES_HOST= адрес сервера
POSTGRES_PORT=5432 

### 3. Запустить проект через Docker-Compose
```bash
docker-compose up --build
```

### 4. Посмотреть логи 
```bash
docker-compose logs

