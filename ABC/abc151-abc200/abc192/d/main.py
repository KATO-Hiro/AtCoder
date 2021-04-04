# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x = input().rstrip()
    digit_count = len(x)
    m = int(input())

    if digit_count == 1:
        if int(x) <= m:
            print(1)
            exit()
        else:
            print(0)
            exit()

    d = 0

    for xi in x:
        d = max(d, int(xi))

    ok = d
    ng = m + 1

    while (ng - ok) > 1:
        wj = (ok + ng) // 2
        summed = 0

        for xi in x:
            summed = summed * wj + int(xi)

        if summed <= m:
            ok = wj
        else:
            ng = wj

    print(ok - d)


if __name__ == "__main__":
    main()
