# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    ans = 0

    for count in c.values():
        mC2 = count * (count - 1) // 2
        ans += mC2 * (n - count)

    print(ans)


if __name__ == "__main__":
    main()
