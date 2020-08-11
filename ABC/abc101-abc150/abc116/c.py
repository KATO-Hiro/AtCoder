# -*- coding: utf-8 -*-


def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = h[0]

    for i in range(1, n):
        ans += max(0, h[i] - h[i - 1])

    print(ans)


if __name__ == '__main__':
    main()
