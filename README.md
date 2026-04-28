# 🚀 NEPSE API Pro — The Ultimate Nepal Stock Exchange API by Diwas Khatri

<p align="center">
  <img src="https://capsule-render.vercel.app/render?type=waving&color=gradient&height=200&section=header&text=NEPSE%20API%20PRO&fontSize=80&animation=fadeIn&fontAlignY=35" width="100%" />
</p>

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![PyPI](https://img.shields.io/pypi/v/api-nepse?style=for-the-badge)](https://pypi.org/project/api-nepse/)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/BalochLeader)

**NEPSE API Pro** is the most advanced, high-performance, and comprehensive unofficial API for the **Nepal Stock Exchange (NEPSE)**. Developed by **Diwas Khatri**, this tool is designed for developers, financial analysts, and algorithmic traders who need reliable, real-time access to the Nepal stock market.

---

## 🔥 Why Choose NEPSE API Pro?

This is not just another scraper. It is a production-ready API that handles the complexities of the NEPSE website automatically.

- ⚡ **Real-time Market Data**: Get live stock prices, LTP, and market status instantly.
- 📊 **Comprehensive Coverage**: Access Today's Price, Indices, Sub-Indices, and Floorsheet data.
- 🏢 **Deep Insights**: Detailed market depth, company profiles, and security lists.
- 🔝 **Performance Tracking**: Real-time Top Gainers, Losers, Turnover, Volume, and Transactions.
- 🛡️ **Advanced Security**: Automatically handles NEPSE's complex authentication and WASM-based token parsing.
- 🔄 **Anti-Blocking**: Built-in User-Agent rotation and optimized request handling.

---

## 🚀 Quick Start

### 1. Installation

Install the official `api-nepse` package from PyPI:

```bash
pip install api-nepse
```

### 2. Launch the API Server

Run the server with a single command:

```bash
api-nepse
```

Your API will be live at `http://localhost:8080`. View the interactive documentation at `http://localhost:8080/docs`.

---

## 💻 Developer Integration

### Python Example
```python
import requests

# Fetch Today's Price from NEPSE
response = requests.get("http://localhost:8080/api/v1/market/today-price")
data = response.json()

if data["status"] == "success":
    for stock in data["data"]:
        print(f"{stock['symbol']}: Rs. {stock['lastTradedPrice']}")
```

### JavaScript (Fetch) Example
```javascript
// Get Live Market Status
fetch('http://localhost:8080/api/v1/market/live')
  .then(res => res.json())
  .then(json => console.log("Live Data:", json.data))
  .catch(err => console.error("API Error:", err));
```

---

## 📖 Key API Endpoints

| Category | Endpoint | Description |
| :--- | :--- | :--- |
| **Market** | `GET /api/v1/market/status` | Real-time Market Open/Closed status |
| **Market** | `GET /api/v1/market/today-price` | Complete Today's Price list |
| **Market** | `GET /api/v1/market/live` | Live stock prices during trading hours |
| **Indices** | `GET /api/v1/indices` | All NEPSE and Sub-Indices |
| **Performers** | `GET /api/v1/top/gainers` | Top 10 Gaining stocks |
| **Advanced** | `GET /api/v1/market/floorsheet` | Real-time Floorsheet transactions |

---

## 👨‍💻 About the Developer

**Diwas Khatri** is a passionate developer specializing in automation, financial tools, and API development. 

- 🌍 **GitHub**: [BalochLeader](https://github.com/BalochLeader)
- 📢 **Telegram**: [@BalochLeader](https://t.me/BalochLeader)
- 📧 **Contact**: Reach out for custom API solutions or collaborations.

---

## 📜 License & Disclaimer

This project is licensed under the **MIT License**.

**Disclaimer**: This is an **unofficial** API. It is intended for educational and informational purposes only. It is not affiliated with or endorsed by the Nepal Stock Exchange (NEPSE). Use responsibly.

---

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=BalochLeader-NEPSE-API&color=blueviolet&style=flat-square&label=REPO+VIEWS" alt="NEPSE API Views" />
</p>
