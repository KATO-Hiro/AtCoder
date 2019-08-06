# -*- coding: utf-8 -*-


def main():
    n, k, m, r = map(int, input().split())
    s = sorted([int(input()) for _ in range(n - 1)], reverse=True)
    diff = (k * r) - sum(s[:k - 1])

    if diff <= 0:
        print(0)
    elif diff - max(s[k - 1], m) > 0:
        print(-1)
    else:
        print(diff)


if __name__ == '__main__':
    main()
