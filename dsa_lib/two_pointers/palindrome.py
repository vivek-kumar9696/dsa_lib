def check_palindrome(text: str) -> bool:
    text = "".join(filter(str.isalnum, text.replace(" ", ""))).lower()
    init = 0
    fin = len(text) - 1

    while init <= fin:
        if text[init] == text[fin]:
            init += 1
            fin -= 1
            continue
        else:
            return False
    return True
