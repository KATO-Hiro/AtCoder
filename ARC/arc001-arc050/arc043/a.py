# -*- coding: utf-8 -*-


def main():
    n, a, b = map(int, input().split())
    s = [int(input()) for _ in range(n)]
    s_max = max(s)
    s_min = min(s)

    if s_max == s_min:
        print(-1)
    else:
        p = b / (s_max - s_min)
        s_sum = sum(s)
        q = a - p * s_sum / n
        print(p, q)


if __name__ == '__main__':
    main()
