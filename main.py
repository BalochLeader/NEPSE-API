from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from nepse import Nepse
import uvicorn
from typing import Optional, List, Dict, Any
from datetime import datetime
import json

app = FastAPI(
    title="NEPSE API - Unofficial Nepal Stock Exchange API",
    description="A comprehensive unofficial API for real-time Nepal Stock Exchange (NEPSE) data with live market prices, indices, company information, and more.",
    version="1.0.0"
)

nepse = Nepse()
nepse.setTLSVerification(False)

# Developer Information
DEVELOPER_INFO = {
    "name": "Gunpark",
    "instagram": "@gunpark_xd",
    "version": "1.0.0"
}

def create_response(data: Any, endpoint: str, status: str = "success"):
    """Create a standardized response format with developer info."""
    return {
        "status": status,
        "timestamp": datetime.now().isoformat(),
        "endpoint": endpoint,
        "developer": DEVELOPER_INFO,
        "data": data
    }

@app.get("/", tags=["General"])
def read_root():
    """Welcome endpoint with API information."""
    return create_response(
        {
            "message": "Welcome to NEPSE API - Unofficial Nepal Stock Exchange API",
            "description": "Real-time market data, indices, company information, and more",
            "version": "1.0.0",
            "documentation": "/docs"
        },
        "/"
    )

# ===================== MARKET SUMMARY ENDPOINTS =====================

@app.get("/api/v1/summary", tags=["Market Summary"])
def get_summary():
    """Get overall market summary including turnover, transactions, and capitalization."""
    try:
        data = nepse.getSummary()
        summary = {obj["detail"]: obj["value"] for obj in data}
        return create_response(summary, "/api/v1/summary")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/market-status", tags=["Market Summary"])
def get_market_status():
    """Check if NEPSE market is currently open or closed."""
    try:
        data = nepse.isNepseOpen()
        return create_response(data, "/api/v1/market-status")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ===================== INDICES ENDPOINTS =====================

@app.get("/api/v1/indices", tags=["Indices"])
def get_indices():
    """Get NEPSE main index data."""
    try:
        data = nepse.getNepseIndex()
        indices = {obj["index"]: obj for obj in data}
        return create_response(indices, "/api/v1/indices")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/sub-indices", tags=["Indices"])
def get_subindices():
    """Get sector-wise sub-indices (Banking, Finance, Hydro, etc.)."""
    try:
        data = nepse.getNepseSubIndices()
        subindices = {obj["index"]: obj for obj in data}
        return create_response(subindices, "/api/v1/sub-indices")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ===================== TOP PERFORMERS ENDPOINTS =====================

@app.get("/api/v1/top-gainers", tags=["Top Performers"])
def get_top_gainers(limit: Optional[int] = 10):
    """Get top gaining stocks. Returns top 10 by default."""
    try:
        data = nepse.getTopGainers()
        top_gainers = data[:limit] if limit else data
        return create_response(
            {
                "count": len(top_gainers),
                "gainers": top_gainers
            },
            "/api/v1/top-gainers"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/top-losers", tags=["Top Performers"])
def get_top_losers(limit: Optional[int] = 10):
    """Get top losing stocks. Returns top 10 by default."""
    try:
        data = nepse.getTopLosers()
        top_losers = data[:limit] if limit else data
        return create_response(
            {
                "count": len(top_losers),
                "losers": top_losers
            },
            "/api/v1/top-losers"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/top-traded", tags=["Top Performers"])
def get_top_traded():
    """Get top traded stocks by volume."""
    try:
        data = nepse.getTopTenTradeScrips()
        return create_response(
            {
                "count": len(data),
                "stocks": data
            },
            "/api/v1/top-traded"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/top-turnover", tags=["Top Performers"])
def get_top_turnover():
    """Get stocks with highest turnover value."""
    try:
        data = nepse.getTopTenTurnoverScrips()
        return create_response(
            {
                "count": len(data),
                "stocks": data
            },
            "/api/v1/top-turnover"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/top-transactions", tags=["Top Performers"])
def get_top_transactions():
    """Get stocks with highest transaction count."""
    try:
        data = nepse.getTopTenTransactionScrips()
        return create_response(
            {
                "count": len(data),
                "stocks": data
            },
            "/api/v1/top-transactions"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ===================== LIVE MARKET ENDPOINTS =====================

@app.get("/api/v1/live-market", tags=["Live Market"])
def get_live_market():
    """Get live market data for all traded securities."""
    try:
        data = nepse.getLiveMarket()
        return create_response(
            {
                "count": len(data) if isinstance(data, list) else 1,
                "market": data
            },
            "/api/v1/live-market"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/price-volume", tags=["Live Market"])
def get_price_volume():
    """Get price and volume data for all securities."""
    try:
        data = nepse.getPriceVolume()
        return create_response(
            {
                "count": len(data),
                "data": data
            },
            "/api/v1/price-volume"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ===================== COMPANY & SECURITY ENDPOINTS =====================

@app.get("/api/v1/companies", tags=["Companies"])
def get_company_list():
    """Get list of all listed companies on NEPSE."""
    try:
        data = nepse.getCompanyList()
        return create_response(
            {
                "total_companies": len(data),
                "companies": data
            },
            "/api/v1/companies"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/securities", tags=["Companies"])
def get_security_list():
    """Get list of all securities (including promoter shares)."""
    try:
        data = nepse.getSecurityList()
        return create_response(
            {
                "total_securities": len(data),
                "securities": data
            },
            "/api/v1/securities"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ===================== MARKET DEPTH ENDPOINTS =====================

@app.get("/api/v1/market-depth/{symbol}", tags=["Market Depth"])
def get_market_depth(symbol: str):
    """Get market depth (buy/sell orders) for a specific symbol."""
    try:
        symbol = symbol.upper()
        data = nepse.getSymbolMarketDepth(symbol)
        return create_response(
            {
                "symbol": symbol,
                "depth": data
            },
            f"/api/v1/market-depth/{symbol}"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching market depth for {symbol}: {str(e)}")

# ===================== SUPPLY & DEMAND ENDPOINTS =====================

@app.get("/api/v1/supply-demand", tags=["Market Data"])
def get_supply_demand():
    """Get supply and demand data for the market."""
    try:
        data = nepse.getSupplyDemand()
        return create_response(data, "/api/v1/supply-demand")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ===================== STATISTICS ENDPOINTS =====================

@app.get("/api/v1/statistics", tags=["Statistics"])
def get_statistics():
    """Get comprehensive market statistics."""
    try:
        summary = nepse.getSummary()
        indices = nepse.getNepseIndex()
        gainers = nepse.getTopGainers()
        losers = nepse.getTopLosers()
        
        summary_dict = {obj["detail"]: obj["value"] for obj in summary}
        
        stats = {
            "market_summary": summary_dict,
            "indices": {obj["index"]: obj for obj in indices},
            "top_gainers_count": len(gainers),
            "top_losers_count": len(losers),
            "top_gainer": gainers[0] if gainers else None,
            "top_loser": losers[0] if losers else None
        }
        
        return create_response(stats, "/api/v1/statistics")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ===================== HEALTH CHECK =====================

@app.get("/health", tags=["General"])
def health_check():
    """Health check endpoint."""
    return create_response(
        {
            "status": "healthy",
            "service": "NEPSE API",
            "version": "1.0.0"
        },
        "/health"
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
