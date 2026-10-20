def echo_validator(text: str) -> bool:
    if not text:
        return False
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
