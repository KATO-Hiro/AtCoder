# -*- coding: utf-8 -*-


def main():
    n, k, m, r = map(int, input().split())
    s = sorted([int(input()) for _ in range(n - 1)], reverse=True)

    if sum(s[:k]) >= k * r:
        print(0)
    elif sum(s[:k - 1]) + m < k * r:
        print(-1)
    else:
        print(r * k - sum(s[:k - 1]))


if __name__ == '__main__':
    main()
