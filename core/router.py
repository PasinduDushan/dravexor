import time
import random
from threading import Lock

class DravexorRouter:
    def __init__(self, nodes):
        self.nodes = nodes
        self.index = 0
        self.lock = Lock()

    def route(self, payload):
        with self.lock:
            target = self.nodes[self.index % len(self.nodes)]
            self.index += 1
        latency = random.uniform(0.001, 0.05)
        time.sleep(latency)
        return target.handle(payload)
