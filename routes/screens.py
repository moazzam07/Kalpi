from fastapi import APIRouter
from schemas import ScreeningCriteria
import utils

router = APIRouter()

@router.get("/")
async def get_all_screens(limit: int = 100, skip: int = 0):
    return await utils.get_screens(limit=limit, skip=skip)

@router.post("/create")
async def create_screen(screen: ScreeningCriteria):
    return await utils.create_screen(screen.dict())

@router.get("/{screen_name}/run")
async def run_screen(screen_name: str, limit: int = 100, skip: int = 0):
    screen = await utils.get_screen(screen_name)
    
    condition = screen.get("conditions", {})
    matching_stocks = await utils.get_stocks(condition, limit=limit, skip=skip)
    return matching_stocks
