import os
import httpx

ABUSEIPDB_API_KEY = os.getenv("ABUSEIPDB_API_KEY", "")
ABUSEIPDB_URL = "https://api.abuseipdb.com/api/v2/check"


async def get_abuse_confidence(ip: str) -> int:
    """
    Returns AbuseIPDB abuseConfidenceScore for an IP (0–100).
    """
    if not ABUSEIPDB_API_KEY:
        return 0

    headers = {
        "Key": ABUSEIPDB_API_KEY,
        "Accept": "application/json",
    }
    params = {
        "ipAddress": ip,
        "maxAgeInDays": 7,
    }

    async with httpx.AsyncClient(timeout=5.0) as client:
        resp = await client.get(ABUSEIPDB_URL, headers=headers, params=params)
        resp.raise_for_status()
        data = resp.json()
        return int(data["data"]["abuseConfidenceScore"])
