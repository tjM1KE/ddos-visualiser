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
