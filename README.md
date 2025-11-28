# 🌐 Live DDoS Attack Map Visualizer

A defensive **DDoS attack map** that shows suspicious IPs as arcs on a 3D globe, using:

- 🐍 **FastAPI** backend (Python)
- 🧠 Simple ML-based DDoS scoring
- 🌍 **GeoIP** (MaxMind GeoLite2)
- 🧊 **Aceternity UI GitHub Globe** (React + three.js)
- ⚛️ **Next.js + Tailwind CSS** frontend

> ⚠️ This project is for defensive / educational purposes only.

---

## 🚀 Features

- Live(ish) **attack arcs** on a 3D globe
- **Backend API** (`/arcs`) that returns attack paths in a simple JSON format
- Pluggable **data source** (`get_suspicious_ips`) – start with fake data, later hook up logs
- Room for **ML-based DDoS scoring** with scikit-learn

---

## 🧱 Project Structure

```text
ddos-visualiser/
  backend/   # FastAPI app, ML, GeoIP, AbuseIPDB integration
  frontend/  # Next.js app with Aceternity GitHub Globe

```

# 🌐 Live DDoS Attack Map Visualizer

<p align="center">
  <img src="assets/globe-project-ezgif.com-video-to-gif-converter.gif" alt="Project preview" width="200">
</p>

---

## 🧱 Tech Stack

### Backend

- **Python 3**
- **FastAPI** – REST API
- **Uvicorn** – ASGI server
- **Pydantic / pydantic-settings** – settings & data models
- **geoip2** – IP → latitude/longitude (MaxMind GeoLite2)
- **httpx** – async HTTP client (AbuseIPDB, etc.)
- **scikit-learn** (optional) – DDoS confidence scoring model
- **joblib** (optional) – model persistence

### Frontend

- **Next.js** (React)
- **TypeScript**
- **Tailwind CSS**
- **Aceternity UI GitHub Globe** (Three.js + `three-globe`)
- **@react-three/fiber**, **@react-three/drei** – React bindings for Three.js

---

## ⚙️ Getting Started (Local)

> Prereqs:  
> – Python 3.x  
> – Node.js + npm  
> – (Optional) MaxMind GeoLite2 database, AbuseIPDB key

### 1. Clone the repo

```bash
git clone https://github.com/<your-username>/ddos-visualiser.git
cd ddos-visualiser
```

---

##  🧪 Fake Data for Demo
```
  To see arcs immediately, a small block in startup_event seeds fake attack events on startup.
  You can remove this once you hook it up to real logs.
```

---

## 📄 License

This project is licensed under the **MIT License** – see the [`LICENSE`](LICENSE) file for details.
