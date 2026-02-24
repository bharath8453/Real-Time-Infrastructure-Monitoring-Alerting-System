from prometheus_client import Gauge, start_http_server
import psutil
import time

cpu_gauge = Gauge(
    "cpu_usage_percent",
    "CPU usage percentage"
)

if __name__ == "__main__":
    start_http_server(9100)
    print("CPU exporter running on :9100")

    while True:
        cpu = psutil.cpu_percent(interval=1)
        cpu_gauge.set(cpu)
        time.sleep(1)
