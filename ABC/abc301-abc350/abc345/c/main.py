# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    s = input().rstrip()
    t = set(s)
    c = Counter(s)

    ans = 0

    for si in s:
        for key, value in c.items():
            if si == key:
                continue

            ans += value

    ans //= 2

    if len(s) != len(t):
        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
