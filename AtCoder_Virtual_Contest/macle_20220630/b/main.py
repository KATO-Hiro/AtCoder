# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    two = list()
    four = list()

    for key, value in c.items():
        if value >= 4:
            four.append(key)
        if value >= 2:
            two.append(key)

    ans = 0

    if len(four) >= 1:
        ans = max(ans, max(four) ** 2)
    
    if len(two) >= 2:
        t = sorted(two, reverse=True)
        ans = max(ans, t[0] * t[1])

    print(ans)


if __name__ == "__main__":
    main()
