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
- 🔄 **Multiple Headers**: Rotates User-Agents to prevent blocking.

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

---

## 💻 Code Examples

### Python Example
```python
import requests

# Get Today's Price
response = requests.get("http://localhost:8080/api/v1/market/today-price")
data = response.json()

if data["status"] == "success":
    for record in data["data"]:
        print(f"{record['symbol']}: {record['lastTradedPrice']}")
```

### JavaScript (Fetch) Example
```javascript
fetch('http://localhost:8080/api/v1/market/live')
  .then(response => response.json())
  .then(data => console.log(data.data))
  .catch(error => console.error('Error:', error));
```

---

## 🌐 How to Host

### 1. Local Hosting
Simply run `api-nepse` on your local machine. Ensure port 8080 is open.

### 2. Cloud Hosting (Heroku / Render / Railway)
1. Fork this repository.
2. Connect your GitHub to the hosting platform.
3. Set the start command to:
   ```bash
   uvicorn api_nepse.main:app --host 0.0.0.0 --port $PORT
   ```

### 3. Docker Hosting
Use the following `Dockerfile`:
```dockerfile
FROM python:3.9
RUN pip install api-nepse
EXPOSE 8080
CMD ["api-nepse"]
```

---

## 📖 API Endpoints

👉 **[http://localhost:8080/docs](http://localhost:8080/docs)**

| Category | Endpoint | Description |
| :--- | :--- | :--- |
| **Market** | `GET /api/v1/market/status` | Check if market is OPEN/CLOSED |
| **Market** | `GET /api/v1/market/today-price` | Full Today's Price sheet |
| **Market** | `GET /api/v1/market/live` | Real-time live stock prices |
| **Indices** | `GET /api/v1/indices` | All NEPSE Indices |
| **Performers** | `GET /api/v1/top/gainers` | Top 10 Gaining stocks |
| **Advanced** | `GET /api/v1/market/floorsheet` | Latest Floorsheet data |

---

## 👨‍💻 Developer

**Gunpark**
- 📸 Instagram: [@gunpark_xd](https://instagram.com/gunpark_xd)
- 💻 GitHub: [BalochLeader](https://github.com/BalochLeader)

---

## 📜 License

This project is licensed under the **MIT License**.

## ⚠️ Disclaimer

This is an **unofficial** API. Use for informational purposes only. Not affiliated with NEPSE.
