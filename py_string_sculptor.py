def string_sculptor(text: str) -> str:
    result = ""
    i = 0;
    for c in text:
        if c == " ":
            i = 0
            result += c;
        elif c.isalpha():
            if i % 2 != 0:
                result += c.upper()
            else:
                result += c.lower()
            i += 1
        else:
            result += c
    return result

