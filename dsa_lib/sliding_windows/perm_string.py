from typing import Dict


def find_perms(src_str: str, tgt_str: str) -> bool:
    fm_tgt = create_fm(tgt_str)
    window_init = 0
    window_fin = len(tgt_str)
    for i in range(len(src_str) - len(tgt_str) + 1):
        fm_src = create_fm(src_str[window_init + i : window_fin + i])
        if fm_src == fm_tgt:
            return True

    return False


def create_fm(string: str) -> Dict:
    res = {}
    for ele in string:
        if ele in res:
            res[ele] += 1
        else:
            res[ele] = 1

    return res
