def hidenp(small: str, big: str) -> bool:
    it = iter(big)
    return all(ch in it for ch in small)
