# -*- coding: utf-8 -*-


def main():
    from itertools import combinations

    n = int(input())
    d = list(map(int, input().split()))
    ans = 0

    for first, second in combinations(d, 2):
        ans += first * second

    print(ans)


if __name__ == '__main__':
    main()
