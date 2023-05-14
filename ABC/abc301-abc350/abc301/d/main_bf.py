# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import product

    input = sys.stdin.readline

    s = input().rstrip()
    m = len(s)
    n = int(input())
    patterns = product(["0", "1"], repeat=m)
    ans = [-1]

    for pattern in patterns:
        ok = True

        for si, pi in zip(s, pattern):
            if si != "?" and si != pi:
                ok = False
                break

        if ok:
            tmp = 0

            for i, pi in enumerate(pattern):
                if pi == "1":
                    tmp += 1 << (m - i - 1)

            if tmp <= n:
                ans.append(tmp)

    print(max(ans))


if __name__ == "__main__":
    main()
