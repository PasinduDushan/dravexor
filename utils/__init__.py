class Dravexor:
    def __init__(self, nodes=4):
        self.nodes = [f"DravexorNode-{i}" for i in range(nodes)]
        self.ptr = 0

    def route(self, payload):
        target = self.nodes[self.ptr % len(self.nodes)]
        print(f"[Dravexor] Routed '{payload}' to {target}")
        self.ptr += 1

    def route_many(self, payloads):
        print(f"[Dravexor] Routing batch of {len(payloads)} packets")
        for p in payloads:
            self.route(p)

    def reset(self):
        self.ptr = 0