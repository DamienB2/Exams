def pattern_tracker(text: str) -> int:
    count = 0
    for i in range(len(text) - 1):
        c1, c2 = text[i], text[i + 1]

        if c1.isdigit() and c2.isdigit():
            if int(c2) == int(c1) + 1:
                count += 1

    return count
