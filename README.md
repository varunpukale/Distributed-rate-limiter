# 🚀 Distributed Rate Limiter

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Redis](https://img.shields.io/badge/Redis-Enabled-red)
![Flask](https://img.shields.io/badge/Flask-API-green)

A scalable distributed rate limiting system built using **Python, Flask, and Redis**, designed to control API traffic across multiple services in real-time.

---

## 📌 Overview

This project implements a **distributed rate limiting mechanism** using Redis as a centralized store, enabling multiple API instances to enforce request limits consistently.

It prevents abuse, protects backend systems, and ensures fair usage across clients.

---

## ⚙️ Tech Stack

- Python
- Flask (API Layer)
- Redis (In-memory datastore)
- REST APIs

---

## 🏗️ Architecture

```
Client → Flask API → Rate Limiter → Redis → Response
```

- Flask handles incoming requests  
- Rate limiter checks request count  
- Redis stores request counters with expiration  
- API returns **200 (allowed)** or **429 (rate limited)**  

---

## 🔥 Features

- Distributed rate limiting using Redis  
- Fixed window algorithm implementation  
- Real-time request tracking  
- Scalable across multiple instances  
- O(1) request processing  
- Clean modular architecture  

---

## 📂 Project Structure

```
api/
 ├── server.py
 ├── limiter/
 │     └── rate_limiter.py
 └── utils/
       └── redis_client.py
```

---

## 🚀 How It Works

1. Each request is associated with a user ID  
2. Redis key stores request count per user  
3. Expiry is set for time window (e.g., 60 sec)  
4. If limit exceeded → request blocked  

---

## ▶️ Running Locally

Install dependencies:
```bash
pip install -r requirements.txt
```

Start Redis:
```bash
redis-server
```

Run API:
```bash
python api/server.py
```

Test endpoint:
```
http://localhost:5000/request?user_id=123
```

---

## 📊 Example Responses

✅ Allowed:
```json
{
  "message": "Request allowed"
}
```

❌ Rate Limited:
```json
{
  "error": "Rate limit exceeded"
}
```

---

## 🚀 Future Improvements

- Sliding window / token bucket algorithm  
- Authentication-based rate limiting  
- Kubernetes deployment  
- Monitoring & alerting  

---

## 👨‍💻 Author

**Varun Pukale**
