from typing import Optional
from fastapi import HTTPException
import schemas
from db import db

def clean_mongo_docs(docs):
    return [{**doc, "_id": str(doc["_id"])} for doc in docs]

async def create_stock(stock: schemas.Stock):
    result = await db.stocks.insert_one(stock)
    return str(result.inserted_id)

async def get_stocks(screen_criteria: Optional[dict] = None, limit: int = 100):
    stocks = await db.stocks.find(screen_criteria).to_list(limit)
    return clean_mongo_docs(stocks)

async def create_screen(criteria: schemas.ScreeningCriteria):
    result = await db.screens.insert_one(criteria)
    return str(result.inserted_id)

async def get_screens(limit: int = 100):
    screens = await db.screens.find().to_list(limit)
    return clean_mongo_docs(screens)

async def get_screen(screen_name: str):
    screen = await db.screens.find_one({"name": screen_name})
    if not screen:
        raise HTTPException(status_code=404, detail="Screening criteria not found")
    return screen