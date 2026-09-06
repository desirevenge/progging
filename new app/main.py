from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

BALANCE = {}


class WalletCreate(BaseModel):
    """Тело запроса для создания кошелька или операции с суммой."""
    name: str
    amount: float = 0.0


# ---------- Управление кошельками ----------

@app.post("/wallets", status_code=201)
def create_wallet(payload: WalletCreate):
    """Создать новый кошелёк с начальным балансом."""
    if payload.name in BALANCE:
        raise HTTPException(
            status_code=409,
            detail=f"Wallet '{payload.name}' already exists",
        )
    BALANCE[payload.name] = payload.amount
    return {"wallet": payload.name, "balance": payload.amount}


@app.delete("/wallets/{wallet_name}")
def delete_wallet(wallet_name: str):
    """Удалить кошелёк."""
    if wallet_name not in BALANCE:
        raise HTTPException(
            status_code=404,
            detail=f"Wallet '{wallet_name}' not found",
        )
    removed = BALANCE.pop(wallet_name)
    return {"deleted": wallet_name, "was_balance": removed}


# ---------- Операции с деньгами ----------

@app.post("/wallets/{wallet_name}/deposit")
def deposit(wallet_name: str, payload: WalletCreate):
    """Пополнить кошелёк."""
    if wallet_name not in BALANCE:
        raise HTTPException(
            status_code=404,
            detail=f"Wallet '{wallet_name}' not found",
        )
    if payload.amount < 0:
        raise HTTPException(status_code=422, detail="Amount cannot be negative")
    BALANCE[wallet_name] += payload.amount
    return {"wallet": wallet_name, "balance": BALANCE[wallet_name]}


@app.post("/wallets/{wallet_name}/withdraw")
def withdraw(wallet_name: str, payload: WalletCreate):
    """Снять деньги с кошелька."""
    if wallet_name not in BALANCE:
        raise HTTPException(
            status_code=404,
            detail=f"Wallet '{wallet_name}' not found",
        )
    if payload.amount < 0:
        raise HTTPException(status_code=422, detail="Amount cannot be negative")
    if BALANCE[wallet_name] < payload.amount:
        raise HTTPException(status_code=400, detail="Not enough funds")
    BALANCE[wallet_name] -= payload.amount
    return {"wallet": wallet_name, "balance": BALANCE[wallet_name]}


# ---------- Просмотр балансов ----------

@app.get("/balance")
def get_total_balance():
    """Общий баланс по всем кошелькам."""
    return {"total_balance": sum(BALANCE.values())}


@app.get("/balance/{wallet_name}")
def get_balance(wallet_name: str):
    """Баланс конкретного кошелька.

    Для кошелька "main" возвращается ключ main_balance,
    для остальных — other_balance.
    """
    if wallet_name not in BALANCE:
        raise HTTPException(
            status_code=404,
            detail=f"Wallet '{wallet_name}' not found",
        )
    if wallet_name == "main":
        return {"main_balance": BALANCE[wallet_name]}
    return {"other_balance": BALANCE[wallet_name]}
    