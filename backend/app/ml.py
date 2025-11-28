from typing import Dict


def score_ddos(features: Dict) -> float:
    """
    Simple placeholder "model". Replace with a real trained model later.
    """
    req_rate = features.get("req_rate", 0)
    abuse_confidence = features.get("abuse_confidence", 0)
    unique_ports = features.get("unique_ports", 1)

    score = 0.0
    score += min(req_rate / 2000.0, 1.0)          # 0-1 from request rate
    score += abuse_confidence / 100.0             # 0-1 from AbuseIPDB
    if unique_ports > 50:
        score += 0.2

    # Clamp to [0,1]
    return max(0.0, min(score, 1.0))
