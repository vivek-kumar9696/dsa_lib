from typing import List


def encode_string(strings: List[str]) -> str:
    res = ""
    for string in strings:
        res += f"{len(string):04b}" + string
    return res


def decode_string(code: str) -> List[str]:
    res = []
    while code:
        length = int(code[0:4], 2)
        word = code[4 : 4 + length]
        res.append(word)
        code = code[4 + length :]
    return res
