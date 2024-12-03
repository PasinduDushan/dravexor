import time

class MetricsCollector:
    def __init__(self):
        self.records = []

    def log(self, message):
        ts = time.strftime("%H:%M:%S", time.localtime())
        self.records.append(f"[{ts}] {message}")
        print(f"[Metrics] {message}")

    def dump(self):
        return "\n".join(self.records)
