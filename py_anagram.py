def anagram(s1: str, s2: str) -> bool:
    s1_cleaned = sorted(s1.replace(" ", "").lower())
    s2_cleaned = sorted(s2.replace(" ", "").lower())
    return s1_cleaned == s2_cleaned
