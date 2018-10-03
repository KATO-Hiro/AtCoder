# -*- coding: utf-8 -*-


def main():
    from collections import Counter

    n = int(input())
    a = Counter([int(input()) for _ in range(n)])
    ans = 0

    for key, value in a.items():
        if value % 2 == 1:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
