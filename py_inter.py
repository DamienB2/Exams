def inter(s1: str, s2: str) -> str:
    res = ""

    for c in s1:
        if c not in res and c in s2:
            res += c
    return res

