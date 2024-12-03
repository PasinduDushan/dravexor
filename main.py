from core.router import DravexorRouter
from core.node import InferenceNode
from utils.metrics import MetricsCollector
import toml

def load_config(path="config/default.toml"):
    return toml.load(path)

def main():
    cfg = load_config()
    nodes = [InferenceNode(f"Node-{i}") for i in range(cfg["nodes"]["count"])]
    router = DravexorRouter(nodes)
    metrics = MetricsCollector()

    payloads = [f"Payload-{i}" for i in range(cfg["system"]["batch_size"])]
    for p in payloads:
        result = router.route(p)
        metrics.log(result)

    print("\n--- Dumping logs ---")
    print(metrics.dump())

if __name__ == "__main__":
    main()
