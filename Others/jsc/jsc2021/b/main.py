# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = list()

    for key, value in Counter(a + b).items():
        if value == 1:
            ans.append(key)

    print(*sorted(ans))


if __name__ == "__main__":
    main()
