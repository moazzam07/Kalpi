from fastapi import FastAPI

from routes import screen, stocks
import uvicorn

app = FastAPI(title="Financial Screener API")

app.include_router(screen.router, prefix="/screens", tags=["Screening Criteria"])
app.include_router(stocks.router, prefix="/stocks", tags=["Stocks"])

@app.get("/")
def root():
    return {"message": "Welcome to the Financial Screener API"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)