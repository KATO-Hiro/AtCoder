# -*- coding: utf-8 -*-


def main():
    from collections import Counter

    n = int(input())
    a = list(map(int, input().split()))
    b = Counter(a)
    ans = 0

    for key, value in b.items():
        if value > key:
            ans += value - key
        elif value < key:
            ans += value

    print(ans)


if __name__ == '__main__':
    main()
