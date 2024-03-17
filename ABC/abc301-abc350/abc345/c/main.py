# -*- coding: utf-8 -*-


def nC2(n: int):
    return n * (n - 1) // 2


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    s = input().rstrip()
    n = len(s)
    c = Counter(s)
    same, diff = 0, 0

    for value in c.values():
        same += nC2(value)

    ans = nC2(n) - same

    if same > 0:
        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
