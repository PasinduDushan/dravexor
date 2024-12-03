import random
import time

class InferenceNode:
    def __init__(self, node_id):
        self.node_id = node_id

    def handle(self, payload):
        compute_time = random.uniform(0.005, 0.2)
        time.sleep(compute_time)
        return f"[{self.node_id}] processed: {payload}"
