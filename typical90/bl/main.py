# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    
    ans = 0
    b = [0] * n

    for i, (a1, a2) in enumerate(zip(a, a[1:])):
       b[i] = a2 - a1
       ans += abs(b[i])
    
    b = [0] + b + [0]
    
    for i in range(q):
        li, ri, vi = map(int, input().split())

        if li - 1 > 0:
            ans -= abs(b[li - 1])
            b[li - 1] += vi
            ans += abs(b[li - 1])
        if ri < n:
            ans -= abs(b[ri])
            b[ri] -= vi
            ans += abs(b[ri])

        print(ans)


if __name__ == "__main__":
    main()
