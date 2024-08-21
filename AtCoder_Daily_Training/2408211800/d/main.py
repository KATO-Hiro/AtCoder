# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import combinations

    input = sys.stdin.readline

    n = int(input())
    b = bin(n)[2:]
    pos = []

    for i, bi in enumerate(b):
        if bi == "1":
            pos.append(i)

    ans = set()

    for i in range(0, len(pos) + 1):
        for pattern in combinations(pos, i):
            base = list(b)

            for pi in pattern:
                base[pi] = "0"

            ans.add(int("".join(base), 2))

    ans = sorted(ans)
    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()
