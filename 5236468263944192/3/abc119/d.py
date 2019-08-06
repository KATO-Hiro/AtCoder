# -*- coding: utf-8 -*-


def main():
    from bisect import bisect

    a, b, q = map(int, input().split())
    s = [int(input()) for _ in range(a)]
    t = [int(input()) for _ in range(b)]
    x = [int(input()) for _ in range(q)]
    # print(s, t, x)

    for xi in x:
        si = bisect(s, xi)
        ti = bisect(t, xi)
        s_left = abs(s[max(0, si - 1)] - xi)
        s_right = abs(s[min(si, a - 1)] - xi)
        t_left = abs(t[max(0, ti - 1)] - xi)
        t_right = abs(t[min(ti, b - 1)] - xi)
        # print(min(max(s_left, t_left), max(s_right, t_right)))
        print(min(2 * t_left + s_right, 2 * t_right + s_left,
              2 * s_left + t_right, 2 * s_right + t_left))


if __name__ == '__main__':
    main()
