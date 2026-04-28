from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from nepse import Nepse
import uvicorn
from typing import Optional, List, Dict, Any
from datetime import datetime
import asyncio

app = FastAPI(
    title="NEPSE API Pro",
    description="The Ultimate Unofficial NEPSE API by Gunpark",
    version="2.1.0"
)

# Enable CORS to prevent Method Not Allowed or Cross-Origin issues
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

nepse = Nepse()
nepse.setTLSVerification(False)

DEVELOPER_INFO = {
    "name": "Gunpark",
    "instagram": "@gunpark_xd",
    "github": "BalochLeader",
    "version": "2.1.0",
    "status": "Official Tagda API"
}

def create_response(data: Any, endpoint: str, status: str = "success"):
    return {
        "status": status,
        "timestamp": datetime.now().isoformat(),
        "endpoint": endpoint,
        "developer": DEVELOPER_INFO,
        "data": data
    }

@app.get("/", tags=["General"])
async def read_root():
    return create_response({"message": "NEPSE API Pro is Running", "docs": "/docs"}, "/")

@app.get("/api/v1/market/status", tags=["Market"])
async def get_market_status():
    try:
        data = nepse.getMarketStatus()
        return create_response(data, "/api/v1/market/status")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/market/summary", tags=["Market"])
async def get_market_summary():
    try:
        data = nepse.getSummary()
        summary = {obj["detail"]: obj["value"] for obj in data}
        return create_response(summary, "/api/v1/market/summary")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/market/today-price", tags=["Market"])
async def get_today_price():
    try:
        data = nepse.getPriceVolume()
        return create_response(data, "/api/v1/market/today-price")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/indices", tags=["Indices"])
async def get_indices():
    try:
        data = nepse.getNepseIndex()
        return create_response(data, "/api/v1/indices")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/companies", tags=["Company"])
async def get_companies():
    try:
        data = nepse.getCompanyList()
        return create_response(data, "/api/v1/companies")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/market/live", tags=["Market"])
async def get_live_market():
    try:
        data = nepse.getLiveMarket()
        return create_response(data, "/api/v1/market/live")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health", tags=["System"])
async def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
