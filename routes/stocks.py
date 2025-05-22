from fastapi import APIRouter
import schemas, utils

router = APIRouter()

@router.get("/")
async def list_stocks(limit: int = 100, skip: int = 0):
    return await utils.get_stocks(limit=limit, skip=skip)

@router.post("/create")
async def create_stock(stock: schemas.Stock):
    stock_data = stock.dict(by_alias=True)
    return await utils.create_stock(stock_data)
