# -*- coding: utf-8 -*-


def main():
    n = int(input())
    p = list(map(int, input().split()))
    value_min = float('inf')
    ans = 0

    for pi in p:
        if value_min > pi:
            ans += 1
            value_min = pi

    print(ans)


if __name__ == '__main__':
    main()
