from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
from nepse import Nepse
import uvicorn
from typing import Optional, List, Dict, Any
from datetime import datetime
import json

app = FastAPI(
    title="NEPSE API Pro - The Ultimate Unofficial Nepal Stock Exchange API",
    description="""
    🚀 **NEPSE API Pro** is the most comprehensive unofficial API for the Nepal Stock Exchange.
    
    Built for developers, traders, and data scientists who need reliable, real-time access to:
    * 📈 **Live Market Prices** & LTP
    * 📊 **Today's Price** (Full Sheet)
    * 🏢 **Company & Security Lists**
    * 📉 **Market Indices & Sub-Indices**
    * 🔝 **Top Gainers, Losers, Turnover, & Volume**
    * 📑 **Market Depth & Order Books**
    * 📅 **Historical Data & More**
    
    Developed with ❤️ by **Gunpark** (IG: @gunpark_xd)
    """,
    version="2.0.0",
    contact={
        "name": "Gunpark",
        "url": "https://instagram.com/gunpark_xd",
    }
)

nepse = Nepse()
nepse.setTLSVerification(False)

# Developer Information for Response
DEVELOPER_INFO = {
    "name": "Gunpark",
    "instagram": "@gunpark_xd",
    "github": "BalochLeader",
    "version": "2.0.0",
    "status": "Official Tagda API"
}

def create_response(data: Any, endpoint: str, status: str = "success"):
    """Standardized response format for maximum professional appeal."""
    return {
        "status": status,
        "timestamp": datetime.now().isoformat(),
        "endpoint": endpoint,
        "developer": DEVELOPER_INFO,
        "data": data
    }

@app.get("/", tags=["General"])
def read_root():
    """API Gateway - Welcome to the Tagda NEPSE API."""
    return create_response(
        {
            "message": "Welcome to NEPSE API Pro",
            "tagline": "Empowering Nepalese Investors with Real-time Data",
            "documentation": "/docs",
            "developer_contact": "IG: @gunpark_xd"
        },
        "/"
    )

# ===================== MARKET STATUS & SUMMARY =====================

@app.get("/api/v1/market/status", tags=["Market Summary"])
def get_market_status():
    """Check if the NEPSE market is currently OPEN or CLOSED."""
    try:
        data = nepse.isNepseOpen()
        return create_response(data, "/api/v1/market/status")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/market/summary", tags=["Market Summary"])
def get_market_summary():
    """Get overall market summary (Turnover, Traded Shares, Transactions, etc.)."""
    try:
        data = nepse.getSummary()
        summary = {obj["detail"]: obj["value"] for obj in data}
        return create_response(summary, "/api/v1/market/summary")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ===================== TODAY'S PRICE (THE BIG ONE) =====================

@app.get("/api/v1/market/today-price", tags=["Market Data"])
def get_today_price(business_date: Optional[str] = None):
    """
    Get the full 'Today's Price' list from NEPSE.
    Optionally provide a business_date (YYYY-MM-DD).
    """
    try:
        # Using getPriceVolume as it provides the core today's price data
        data = nepse.getPriceVolume()
        return create_response(
            {
                "count": len(data),
                "date": business_date or datetime.now().strftime("%Y-%m-%d"),
                "records": data
            },
            "/api/v1/market/today-price"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ===================== INDICES & SECTORS =====================

@app.get("/api/v1/indices", tags=["Indices"])
def get_all_indices():
    """Get all NEPSE Indices (NEPSE, Sensitive, Float, etc.)."""
    try:
        data = nepse.getNepseIndex()
        return create_response(data, "/api/v1/indices")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/sub-indices", tags=["Indices"])
def get_all_sub_indices():
    """Get all Sector-wise Sub-Indices."""
    try:
        data = nepse.getNepseSubIndices()
        return create_response(data, "/api/v1/sub-indices")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ===================== TOP PERFORMERS =====================

@app.get("/api/v1/top/gainers", tags=["Top Performers"])
def get_top_gainers():
    """Get the list of Top 10 Gaining stocks."""
    try:
        data = nepse.getTopGainers()
        return create_response(data, "/api/v1/top/gainers")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/top/losers", tags=["Top Performers"])
def get_top_losers():
    """Get the list of Top 10 Losing stocks."""
    try:
        data = nepse.getTopLosers()
        return create_response(data, "/api/v1/top/losers")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/top/turnover", tags=["Top Performers"])
def get_top_turnover():
    """Get stocks with the highest Turnover."""
    try:
        data = nepse.getTopTenTurnoverScrips()
        return create_response(data, "/api/v1/top/turnover")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/top/volume", tags=["Top Performers"])
def get_top_volume():
    """Get stocks with the highest Traded Volume."""
    try:
        data = nepse.getTopTenTradeScrips()
        return create_response(data, "/api/v1/top/volume")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/top/transactions", tags=["Top Performers"])
def get_top_transactions():
    """Get stocks with the highest number of Transactions."""
    try:
        data = nepse.getTopTenTransactionScrips()
        return create_response(data, "/api/v1/top/transactions")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ===================== COMPANY & SECURITY LISTS =====================

@app.get("/api/v1/companies", tags=["Company Info"])
def get_all_companies():
    """Get a complete list of all listed companies."""
    try:
        data = nepse.getCompanyList()
        return create_response(
            {
                "total": len(data),
                "companies": data
            },
            "/api/v1/companies"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/securities", tags=["Company Info"])
def get_all_securities():
    """Get a complete list of all securities (including debentures, mutual funds)."""
    try:
        data = nepse.getSecurityList()
        return create_response(
            {
                "total": len(data),
                "securities": data
            },
            "/api/v1/securities"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ===================== LIVE MARKET & DEPTH =====================

@app.get("/api/v1/market/live", tags=["Live Market"])
def get_live_market():
    """Get real-time live market prices for all active stocks."""
    try:
        data = nepse.getLiveMarket()
        return create_response(data, "/api/v1/market/live")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/market/depth/{symbol}", tags=["Live Market"])
def get_market_depth(symbol: str):
    """Get the real-time Order Book (Market Depth) for a specific symbol."""
    try:
        symbol = symbol.upper()
        data = nepse.getSymbolMarketDepth(symbol)
        return create_response(data, f"/api/v1/market/depth/{symbol}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch depth for {symbol}")

# ===================== ADVANCED DATA =====================

@app.get("/api/v1/market/supply-demand", tags=["Advanced Data"])
def get_supply_demand():
    """Get market-wide Supply and Demand statistics."""
    try:
        data = nepse.getSupplyDemand()
        return create_response(data, "/api/v1/market/supply-demand")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/market/floorsheet", tags=["Advanced Data"])
async def get_floorsheet():
    """Get the latest Floorsheet data (Recent Transactions)."""
    try:
        # Note: getFloorSheet is async in the library
        data = await nepse.getFloorSheet()
        return create_response(data[:500], "/api/v1/market/floorsheet") # Limit to 500 for API performance
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ===================== HEALTH & SYSTEM =====================

@app.get("/health", tags=["System"])
def health_check():
    """API Health Check."""
    return create_response({"status": "online", "server": "Tagda-NEPSE-Server"}, "/health")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
