# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import product

    input = sys.stdin.readline

    n = int(input())
    b = bin(n)
    ids = [i for i, bi in enumerate(b[2:]) if bi == "1"]
    size = len(ids)
    ans = set()
    c = list(b[2:])

    # nを2進数に変換したときの1の位置を0/1にするかをbit全探索
    for pattern in product([0, 1], repeat=size):
        for pi, id in zip(pattern, ids):
            c[id] = str(pi)

        ans.add(int("".join(c), 2))

    for ans_i in sorted(ans):
        print(ans_i)


if __name__ == "__main__":
    main()
