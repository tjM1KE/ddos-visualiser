import os
import geoip2.database

GEO_DB_PATH = os.getenv("GEOIP2_DB_PATH", "")

_reader = None
if GEO_DB_PATH:
    _reader = geoip2.database.Reader(GEO_DB_PATH)


def geoip_lookup(ip: str):
    """
    Return (lat, lng) for an IP, or (None, None) if not found.
    """
    global _reader
    if _reader is None:
        return None, None

    try:
        resp = _reader.city(ip)
        return resp.location.latitude, resp.location.longitude
    except Exception:
        return None, None
