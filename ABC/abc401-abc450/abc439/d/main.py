# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = 0

    for _ in range(2):
        threes = defaultdict(int)
        sevens = defaultdict(int)

        for ai in a:
            if ai % 7 == 0:
                sevens[ai // 7] += 1
            if ai % 3 == 0:
                threes[ai // 3] += 1
            if ai % 5 == 0:
                p = ai // 5
                ans += sevens[p] * threes[p]

        a = a[::-1]

    print(ans)


if __name__ == "__main__":
    main()
