# 🚀 NEPSE API Pro - The Ultimate Unofficial Nepal Stock Exchange API

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![PyPI](https://img.shields.io/pypi/v/api-nepse?style=for-the-badge)](https://pypi.org/project/api-nepse/)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)](https://instagram.com/gunpark_xd)

**NEPSE API Pro** is a high-performance, ultra-comprehensive unofficial API for the **Nepal Stock Exchange (NEPSE)**. Designed for developers, traders, and financial analysts, it provides seamless access to real-time market data, historical records, and deep market insights.

---

## 🔥 Key Features

- ⚡ **Real-time Data**: Live stock prices, LTP, and market status.
- 📊 **Full Market Coverage**: Today's Price, Indices, Sub-Indices, and Floorsheet.
- 🏢 **Company Insights**: Complete lists of companies, securities, and detailed market depth.
- 🔝 **Performance Tracking**: Top Gainers, Losers, Turnover, Volume, and Transactions.
- 🛠️ **Developer First**: Standardized JSON responses, Swagger UI documentation, and easy integration.
- 🛡️ **Advanced Scraping**: Handles complex NEPSE authentication and WASM-based token parsing automatically.

---

## 🚀 Quick Start

### 1. Installation

Install `api-nepse` directly from PyPI:

```bash
pip install api-nepse
```

### 2. Run the API Server

After installation, you can run the API server using the `api-nepse` command:

```bash
api-nepse
```

The API will be live at `http://localhost:8080`.

### 3. Access API Documentation

Once the server is running, visit the interactive documentation (Swagger UI) at:
👉 **[http://localhost:8080/docs](http://localhost:8080/docs)**

---

## 📖 API Endpoints

All endpoints return data in a standardized JSON format, including a `status`, `timestamp`, `endpoint`, `developer` information, and the `data` payload.

| Category | Endpoint | Description |
| :--- | :--- | :--- |
| **General** | `GET /` | Welcome message and API overview. |
| **System** | `GET /health` | Health check for the API server. |
| **Market** | `GET /api/v1/market/status` | Check if market is OPEN/CLOSED |
| **Market** | `GET /api/v1/market/summary` | Overall market summary. |
| **Market** | `GET /api/v1/market/today-price` | Full Today's Price sheet. |
| **Indices** | `GET /api/v1/indices` | All NEPSE Indices. |
| **Indices** | `GET /api/v1/sub-indices` | Sector-wise sub-indices. |
| **Performers** | `GET /api/v1/top/gainers` | Top 10 Gaining stocks. |
| **Performers** | `GET /api/v1/top/losers` | Top 10 Losing stocks. |
| **Performers** | `GET /api/v1/top/turnover` | Stocks with highest turnover. |
| **Performers** | `GET /api/v1/top/volume` | Stocks with highest traded volume. |
| **Performers** | `GET /api/v1/top/transactions` | Stocks with highest transaction count. |
| **Company** | `GET /api/v1/companies` | Complete list of listed companies. |
| **Company** | `GET /api/v1/securities` | Complete list of all securities. |
| **Live Market** | `GET /api/v1/market/live` | Real-time live market prices for all active stocks. |
| **Live Market** | `GET /api/v1/market/depth/{symbol}` | Real-time Order Book (Market Depth) for a specific symbol. |
| **Advanced Data** | `GET /api/v1/market/supply-demand` | Market-wide Supply and Demand statistics. |
| **Advanced Data** | `GET /api/v1/market/floorsheet` | Latest Floorsheet data (Recent Transactions). |

---

## 🛠️ Technical Architecture

This API is built using **FastAPI** for its asynchronous capabilities and speed. It leverages a custom scraping engine that:
1.  **Authenticates** with NEPSE's servers.
2.  **Parses** dynamic salts using a **WebAssembly (WASM)** module (`css.wasm`).
3.  **Generates** valid tokens to access protected data endpoints.
4.  **Formats** raw data into clean, developer-friendly JSON.

---

## 👨‍💻 Developer

**Gunpark**
- 📸 Instagram: [@gunpark_xd](https://instagram.com/gunpark_xd)
- 💻 GitHub: [BalochLeader](https://github.com/BalochLeader)

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This is an **unofficial** API. It is not affiliated with, maintained by, or endorsed by the Nepal Stock Exchange (NEPSE). Use this data for informational and educational purposes only. For critical financial decisions, always refer to official NEPSE sources.

---

## 🏷️ SEO & Tags

`NEPSE API` `Nepal Stock Exchange` `Nepal Share Market` `Live Stock Prices Nepal` `NEPSE Scraper` `Nepal Finance API` `Python NEPSE` `FastAPI` `Real-time Market Data` `Nepal Investors` `ShareSansar Alternative` `NEPSE Today Price API` `NEPSE Floorsheet API` `api-nepse` `pypi` `python-package`
