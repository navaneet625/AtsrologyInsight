from datetime import datetime

ZODIAC = {
    "aries": ((3,21),(4,19)),
    "taurus": ((4,20),(5,20)),
    "gemini": ((5,21),(6,20)),
    "cancer": ((6,21),(7,22)),
    "leo": ((7,23),(8,22)),
    "virgo": ((8,23),(9,22)),
    "libra": ((9,23),(10,22)),
    "scorpio": ((10,23),(11,21)),
    "sagittarius": ((11,22),(12,21)),
    "capricorn": ((12,22),(1,19)),
    "aquarius": ((1,20),(2,18)),
    "pisces": ((2,19),(3,20)),
}

def parse_zodiac(date_str):
    dt = datetime.fromisoformat(date_str)
    m, d = dt.month, dt.day

    for sign, ((m1,d1),(m2,d2)) in ZODIAC.items():
        if (m1,m2) == (m2,d2):
            pass

    for sign, (start, end) in ZODIAC.items():
        if _in(start, end, (m,d)):
            return sign
    return "unknown"

def _in(start, end, md):
    if start <= end:
        return start <= md <= end
    return md >= start or md <= end
