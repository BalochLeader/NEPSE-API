# NEPSE API - Unofficial Nepal Stock Exchange API

![NEPSE API Logo](https://raw.githubusercontent.com/gunpark/NEPSE-API/main/assets/nepse_logo.png) <!-- Placeholder for a potential logo -->

## Overview
This project provides an **unofficial, real-time API for the Nepal Stock Exchange (NEPSE)**, designed to offer developers and data enthusiasts easy access to critical market data. By intelligently scraping the official NEPSE website and handling complex authentication mechanisms, this API delivers up-to-date information on stock prices, market summaries, company details, and more. It's built with **FastAPI** for high performance and ease of use.

## Features
- **Live Market Data**: Access real-time trading data for all listed securities.
- **Comprehensive Market Summary**: Get daily turnover, total traded shares, transaction counts, and market capitalization.
- **NEPSE Indices**: Retrieve data for the main NEPSE Index and various sector-specific sub-indices (Banking, Finance, Hydro, etc.).
- **Top Performers**: Identify top gaining, losing, traded, turnover, and transaction-heavy stocks.
- **Company Information**: Obtain a complete list of all companies and securities listed on NEPSE.
- **Market Depth**: View detailed buy and sell order information for specific stock symbols.
- **Developer-Friendly**: Clean, well-documented endpoints with standardized JSON responses.

## How to Run

### Prerequisites
- Python 3.8+
- `pip` (Python package installer)

### Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/gunpark/NEPSE-API.git
   cd NEPSE-API
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: `requirements.txt` will be generated and include `fastapi`, `uvicorn`, `httpx[http2]`, `pywasm`, `tqdm`)*

### Running the API Server
To start the API server, navigate to the project root directory and run:
```bash
python main.py
```
The API will be accessible at `http://localhost:8080`.

### Accessing API Documentation
Once the server is running, you can access the interactive API documentation (Swagger UI) at:
[http://localhost:8080/docs](http://localhost:8080/docs)

## API Endpoints
All endpoints return data in a standardized JSON format, including a `status`, `timestamp`, `endpoint`, `developer` information, and the `data` payload.

| Endpoint                               | Description                                                      | Tags             |
|----------------------------------------|------------------------------------------------------------------|------------------|
| `GET /`                                | Welcome message and API overview.                                | General          |
| `GET /health`                          | Health check for the API server.                                 | General          |
| `GET /api/v1/summary`                  | Overall market summary.                                          | Market Summary   |
| `GET /api/v1/market-status`            | Check if NEPSE market is open or closed.                         | Market Summary   |
| `GET /api/v1/indices`                  | Main NEPSE index data.                                           | Indices          |
| `GET /api/v1/sub-indices`              | Sector-wise sub-indices.                                         | Indices          |
| `GET /api/v1/top-gainers`              | Top gaining stocks (default: 10, can be limited with `?limit=`). | Top Performers   |
| `GET /api/v1/top-losers`               | Top losing stocks (default: 10, can be limited with `?limit=`).  | Top Performers   |
| `GET /api/v1/top-traded`               | Top traded stocks by volume.                                     | Top Performers   |
| `GET /api/v1/top-turnover`             | Stocks with highest turnover value.                              | Top Performers   |
| `GET /api/v1/top-transactions`         | Stocks with highest transaction count.                           | Top Performers   |
| `GET /api/v1/live-market`              | Live market data for all securities.                             | Live Market      |
| `GET /api/v1/price-volume`             | Price and volume data for all securities.                        | Live Market      |
| `GET /api/v1/companies`                | List of all listed companies.                                    | Companies        |
| `GET /api/v1/securities`               | List of all securities (including promoter shares).              | Companies        |
| `GET /api/v1/market-depth/{symbol}`    | Market depth for a specific stock symbol (e.g., `/market-depth/NTC`). | Market Depth     |
| `GET /api/v1/supply-demand`            | Market supply and demand data.                                   | Market Data      |
| `GET /api/v1/statistics`               | Comprehensive market statistics.                                 | Statistics       |

## Technical Details
This API leverages the `nepse` library, which is capable of interacting with the official NEPSE data sources. A key aspect of its functionality involves the use of a **WASM (WebAssembly) module (`css.wasm`)** for parsing authentication salts. This mechanism is crucial for generating valid tokens required to access NEPSE's dynamic data endpoints, effectively bypassing anti-scraping measures.

## Developer
- **Name**: Gunpark
- **Instagram**: [@gunpark_xd](https://www.instagram.com/gunpark_xd/)

## License
This project is open-source and available under the MIT License. See the `LICENSE` file for more details.

## Disclaimer
This is an unofficial API and is not affiliated with or endorsed by the Nepal Stock Exchange (NEPSE). Data provided is for informational purposes only and should not be used for financial advice or critical decision-making. The accuracy and availability of data are subject to changes in the official NEPSE website structure and policies.

## Keywords
NEPSE, Nepal Stock Exchange, API, Unofficial API, Stock Market, Live Data, Share Market, Python, FastAPI, Web Scraping, Financial Data, Market Data, Stock Prices, Indices, Top Gainers, Top Losers, Market Depth, Nepal, Investment, Trading, Data Science
