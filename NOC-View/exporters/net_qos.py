from prometheus_client import Gauge, start_http_server
import subprocess
import time
import re

latency_gauge = Gauge(
    "network_latency_ms",
    "Average network latency in milliseconds"
)

packet_loss_gauge = Gauge(
    "packet_loss_percent",
    "Packet loss percentage"
)

def collect():
    result = subprocess.run(
        ["ping", "-n", "5", "8.8.8.8"],
        capture_output=True,
        text=True
    )

    times = re.findall(r"time[=<](\d+)ms", result.stdout)
    if times:
        latency_gauge.set(sum(map(int, times)) / len(times))

    loss = re.search(r"(\d+)% loss", result.stdout)
    if loss:
        packet_loss_gauge.set(float(loss.group(1)))

if __name__ == "__main__":
    start_http_server(9101)
    print("NetQoS exporter running on port 9101")

    while True:
        collect()
        time.sleep(5)

