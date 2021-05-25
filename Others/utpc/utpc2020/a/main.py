# -*- coding: utf-8 -*-


def ok(large_t, x, a):
    before = 0
    t = large_t

    for xi, ai in zip(x, a):
        t = min(large_t, t + xi - before)
        t -= ai

        if t < 0:
            return False

        before = xi
    return True


def main():
    n, l = map(int, input().split())
    x = [0 for _ in range(n)]
    a = [0 for _ in range(n)]

    for i in range(n):
        xi, ai = map(int, input().split())
        x[i] = xi
        a[i] = ai

    lower = 0
    upper = 10 ** 18

    while upper - lower > 1:
        mid = (upper + lower) // 2

        if ok(mid, x, a):
            upper = mid
        else:
            lower = mid

    print(upper)


if __name__ == "__main__":
    main()
