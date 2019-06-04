# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    n = int(input())
    a = Counter(list(map(int, input().split())))
    ans = 0

    for key, value in a.items():
        if key > value:
            ans += value
        elif key < value:
            ans += value - key

    print(ans)


if __name__ == '__main__':
    main()
