# -*- coding: utf-8 -*-


def f(wj, a, k):
    summed = 0

    for ai in a:
        summed += wj // ai
    
    if summed >= k:
        return True
    else:
        return False


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ok = 10 ** 9 + 1
    ng = 1

    while abs(ok - ng) > 1:
        wj = (ok + ng) // 2

        if f(wj, a, k):
            ok = wj
        else:
            ng = wj
        
    print(ok)


if __name__ == "__main__":
    main()
