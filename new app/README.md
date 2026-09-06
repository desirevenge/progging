# Wallet API (FastAPI)

Простое REST-приложение для работы с «кошельками»: создание, удаление, пополнение, снятие и просмотр балансов.

## Запуск

```bash
py -m pip install -r requirements.txt
py -m uvicorn main:app --reload
```

После запуска откройте документацию: http://127.0.0.1:8000/docs (Swagger) или /redoc.

## Эндпоинты

| Метод | Путь                          | Описание                                |
|-------|-------------------------------|-----------------------------------------| 
| POST  | `/wallets`                    | Создать кошелёк `{"name": "...", "amount": 0}` |
| DELETE| `/wallets/{wallet_name}`      | Удалить кошелёк                        |
| POST  | `/wallets/{wallet_name}/deposit`  | Пополнить                            |
| POST  | `/wallets/{wallet_name}/withdraw` | Снять (нельзя уйти в минус)           |
| GET   | `/balance`                    | Суммарный баланс всех кошельков        |
| GET   | `/balance/{wallet_name}`      | Баланс одного кошелька                 |

## Пример

```bash
curl -X POST http://127.0.0.1:8000/wallets -H "Content-Type: application/json" -d '{"name":"main","amount":100}'
curl -X POST http://127.0.0.1:8000/wallets/main/deposit -H "Content-Type: application/json" -d '{"name":"main","amount":50}'
curl http://127.0.0.1:8000/balance/main
curl http://127.0.0.1:8000/balance
```

## Примечание

Данные хранятся в памяти процесса (`BALANCE` в модуле `main.py`) и сбрасываются при перезапуске. Для постоянного хранения подключите SQLite/PostgreSQL через SQLAlchemy.