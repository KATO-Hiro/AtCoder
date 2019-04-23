# -*- coding: utf-8 -*-


def main():
    n = int(input())
    h = list(map(int, input().split()))
    highest = 0
    ans = 0

    for i in range(n):
        if h[i] >= highest:
            ans += 1
            highest = h[i]

    print(ans)


if __name__ == '__main__':
    main()
