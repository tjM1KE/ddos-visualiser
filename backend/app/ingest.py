import random
from typing import List, Dict


async def get_suspicious_ips() -> List[Dict]:
    """
    TEMP: generate random IPs + traffic stats so you can see arcs.

    Replace this with real log aggregation:
      - Parse access logs
      - Aggregate per IP per time window
      - Filter by req_rate, error ratio, etc.
    """
    # ~30% chance of "no new suspicious IPs"
    if random.random() < 0.3:
        return []

    def random_ip():
        return ".".join(str(random.randint(1, 254)) for _ in range(4))

    ips = []
    for _ in range(random.randint(1, 5)):
        ips.append(
            {
                "ip": random_ip(),
                "req_rate": random.randint(500, 4000),
                "unique_ports": random.randint(1, 120),
            }
        )
    return ips
