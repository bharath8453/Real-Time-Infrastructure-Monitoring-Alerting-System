# 🚀 NOCView-PG  
### Real-Time Infrastructure Monitoring & Alerting System

---

## 📌 Project Overview

**NOCView-PG** is a real-time infrastructure monitoring and alerting system designed to monitor:

- CPU Usage
- Network Latency
- Packet Loss

The system uses custom Python exporters, Prometheus for monitoring, and Alertmanager for email notifications, all containerized using Docker Compose.

This project simulates a real-world Network Operations Center (NOC) monitoring environment.

---

## 🎯 Problem Statement

In production environments, infrastructure issues such as:

- High CPU utilization
- Increased network latency
- Packet loss

can cause application downtime and SLA violations.

Manual monitoring is inefficient and reactive. This project provides an automated solution that:

- Continuously monitors system health
- Detects abnormal conditions
- Sends real-time email alerts

---

## 🏗️ System Architecture

Python Exporters  
        ↓  
Prometheus (Scrapes Metrics)  
        ↓  
Alert Rules Evaluation  
        ↓  
Alertmanager  
        ↓  
Gmail SMTP Notification  

---

## 🧩 System Components

### 1️⃣ Custom Python Exporters
- `host_cpu.py` → Monitors CPU usage using psutil
- `net_qos.py` → Measures:
  - Network latency
  - Packet loss

Metrics are exposed in Prometheus format over HTTP.

---

### 2️⃣ Prometheus
- Time-series database
- Pull-based metric collection
- Alert rule evaluation using PromQL
- Containerized via Docker

---

### 3️⃣ Alertmanager
- Receives alerts from Prometheus
- Groups and routes alerts
- Sends email notifications via Gmail SMTP

---

### 4️⃣ Docker & Docker Compose
- Containerized deployment
- Service orchestration
- Simplified startup with a single command

---

Folder Structure
nocview-pg/
│
├── exporters/
│ ├── host_cpu.py
│ └── net_qos.py
│
├── prometheus/
│ ├── prometheus.yml
│ └── rules.yml
│
├── alertmanager/
│ └── alertmanager.yml
│
├── docker-compose.yml
├── requirements.txt
└── README.md


---

## ⚙️ Technologies Used

- Python
- Prometheus
- Alertmanager
- Docker
- Docker Compose
- Gmail SMTP
- psutil
- prometheus-client

---

## 🔧 Setup & Installation

### Prerequisites

- Windows 10/11
- Python 3.11+
- Docker Desktop
- Gmail account with App Password enabled

---

### 1️⃣ Install Dependencies

pip install -r requirements.txt


---

### 2️⃣ Start Exporters

Open two terminals:

Terminal 1:
python exporters/host_cpu.py

Terminal 2:
python exporters/net_qos.py

### 3️⃣ Start Monitoring Stack
docker compose up -d


---

### 4️⃣ Access Services

- Prometheus → http://localhost:9090
- Alertmanager → http://localhost:9093

---

## 🚨 Alert Rules

| Alert | Condition |
|--------|------------|
HighCPUUsage | CPU > 80% for 15 seconds |
HighLatency | Latency above configured threshold |
PacketLossDetected | Packet loss > 2% |

---

## 📧 Email Notification

- Uses Gmail SMTP
- Requires App Password
- Sends alerts during critical conditions
- Can notify when issues are resolved

---

## 🔥 How to Trigger Alerts (Testing)

### Trigger CPU Alert
Generate high CPU load for 20–30 seconds.

### Trigger Network Alert
Temporarily block ICMP traffic to simulate packet loss.

---

## 🧠 Key Features

- Real-time monitoring
- Automated alerting
- Lightweight architecture
- Containerized deployment
- Modular and extensible design

---

## 🚀 Future Enhancements

- Grafana dashboard integration
- Memory and disk monitoring
- Slack/SMS notifications
- AI-based anomaly detection
- Cloud deployment (AWS/Azure)
- Dockerized Python exporters
- CI/CD integration

---

## 📈 Real-World Use Case

This project simulates a Network Operations Center (NOC) monitoring system where infrastructure health must be monitored continuously and alerts must be sent proactively to prevent downtime.

---

## 👨‍💻 Author

Bharath S  
B.E Computer Science  
DevOps | Cloud | Networking | AI Enthusiast  

---

## 📌 Project Highlights

- Built custom Prometheus exporters
- Configured alerting and SMTP email notifications
- Managed container networking
- Implemented Docker Compose orchestration
- Simulated real-world monitoring scenarios

---

## 📜 License

This project is for educational and demonstration purposes.
