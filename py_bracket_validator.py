def bracket_validator(s: str) -> bool:
    brackets = "".join(c for c in s if c in "(){}[]")

    while "()" in brackets or "[]" in brackets or "{}" in brackets:
        brackets = brackets.replace("()", "")
        brackets = brackets.replace("[]", "")
        brackets = brackets.replace("{}", "")

    return not brackets
