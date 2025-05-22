from fastapi import APIRouter
from schemas import ScreeningCriteria
import utils

router = APIRouter()

@router.get("/")
async def get_all_screens():
    return await utils.get_screens()

@router.post("/create")
async def create_screen(screen: ScreeningCriteria):
    return await utils.create_screen(screen.dict())

@router.get("/{screen_name}/run")
async def run_screen(screen_name):
    screen = await utils.get_screen(screen_name)
    
    condition = screen.get("conditions", {})
    matching_stocks = await utils.get_stocks(condition)
    return matching_stocks
