def whisper_cipher(text: str, shift: int) -> str:
    result = ""
    for c in text:
        if c.islower():
            base = ord("a")
        elif c.isupper():
            base = ord("A")
        else:
            result += c
            continue

        position = ord(c) - base
        new_position = (position + shift) % 26
        result += chr(new_position + base)
    return result
