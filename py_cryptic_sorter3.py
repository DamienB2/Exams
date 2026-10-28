def _key(s: str) -> tuple[int, str, int]:
    low = s.lower()
    vowels = sum(1 for c in low if c in "aeiou")
    return (len(s), low, vowels)

def cryptic_sorter(strings: list[str]) -> list[str]:
    result = []
    for string in strings:
        i = len(result)
        # Scan backward until reaching an element that is <= the current string's key
        while i > 0 and _key(result[i - 1]) > _key(string):
            i -= 1
        result.insert(i, string)
    return result
