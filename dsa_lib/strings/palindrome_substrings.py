def find_palindrome_substrings(text: str) -> int:
    ans = 0
    for index, ele in enumerate(text):
        ans += checkPalindrome(text, index, index)
        ans += checkPalindrome(text, index, index + 1)
    return ans


def checkPalindrome(text: str, left: int, right: int) -> int:
    count = 0
    while left >= 0 and right < len(text) and text[left] == text[right]:
        left -= 1
        right += 1
        count += 1
    return count
