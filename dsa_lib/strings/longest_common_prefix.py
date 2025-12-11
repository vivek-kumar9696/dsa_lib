from typing import List


def longest_common_prefix(words: List[str]) -> str:
    if len(words) == 0:
        return ""

    prefix = words[0]

    for word in words[1:]:
        while word.find(prefix) != 0:
            prefix = prefix[:-1]

    return prefix
