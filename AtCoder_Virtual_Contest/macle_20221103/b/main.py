# -*- coding: utf-8 -*-


def f(wj, x, a, b):
    candidate = a * wj + b * len(list(str(wj)))

    if candidate <= x:
        return True
    else:
        return False


def main():
    import sys

    input = sys.stdin.readline

    a, b, x = map(int, input().split())
    ok = 0
    ng = 10 ** 9 + 1

    while abs(ok - ng) > 1:
        wj = (ok + ng) // 2

        if f(wj, x, a, b):
            ok = wj
        else:
            ng = wj
    
    print(ok)


if __name__ == "__main__":
    main()
