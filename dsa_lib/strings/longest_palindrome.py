def find_longest_palindrome(text: str) -> str:
    right = 0
    left = 0
    for index, ele in enumerate(text):
        len1 = check_palindrome(text, index, index)
        len2 = check_palindrome(text, index, index + 1)
        len = max(len1, len2)
        if len >= (right - left) + 1:
            left = index - int((len - 1) / 2)
            right = index + int((len) / 2)

    return text[left : right + 1]


def check_palindrome(text: str, left: int, right: int) -> int:
    while left >= 0 and right < len(text) and text[left] == text[right]:
        left -= 1
        right += 1
    return (right - left) - 1


if __name__ == "__main__":
    result = find_longest_palindrome("a")
    assert result in ["a"]
