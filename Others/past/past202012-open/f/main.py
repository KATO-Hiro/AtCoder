# -*- coding: utf-8 -*-


def main():
    from itertools import product
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())

    patterns = product([0, 1], repeat=n)
    abc = [list(map(int, input().split())) for _ in range(m)]
    ans = 1

    for pattern in patterns:
        case = [index for index, pi in enumerate(pattern, 1) if pi == 1]
        ok = True
        candidate = set()

        for _abc in abc:
            matched = set(case) & set(_abc)
            count = len(matched)

            if count == 2:
                for alpha in _abc:
                    if alpha not in case:
                        candidate.add(alpha)

            if count == 3:
                ok = False

        if ok:
            ans = max(ans, len(candidate))

    print(ans)


if __name__ == "__main__":
    main()
