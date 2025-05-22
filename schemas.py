from pydantic import BaseModel, Field
from typing import Optional, Dict

class ScreeningCriteria(BaseModel):
    name: str
    description: Optional[str]
    conditions: Dict[str, dict] 

class Stock(BaseModel):
    symbol: str
    date: str
    price: float
    market_cap: float
    pe_ratio: Optional[float]
    revenue: Optional[float]