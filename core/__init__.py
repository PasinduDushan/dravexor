import random
import time

class NodeSimulator:
    def __init__(self, id):
        self.id = id

    def receive(self, payload):
        delay = random.uniform(0.01, 0.05)
        time.sleep(delay)
        print(f"[{self.id}] Received '{payload}' after {delay:.3f}s delay")

class RouterEngine:
    def __init__(self, node_count):
        self.nodes = [NodeSimulator(f"SimNode-{i}") for i in range(node_count)]
        self.counter = 0

    def push(self, payload):
        target = self.nodes[self.counter % len(self.nodes)]
        target.receive(payload)
        self.counter += 1

    def broadcast(self, payloads):
        for p in payloads:
            self.push(p)