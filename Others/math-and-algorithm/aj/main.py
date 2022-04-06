# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    imos = [0] * (n + 10)

    for i in range(q):
        li, ri, xi = map(int, input().split())
        imos[li] += xi
        imos[ri + 1] -= xi
    
    b = list(accumulate(imos))[1:n + 1]
    ans = ""

    for b1, b2 in zip(b, b[1:]):
        if b1 > b2:
            ans += ">"
        elif b1 == b2:
            ans += "="
        else:
            ans += "<"

    print(ans)


if __name__ == "__main__":
    main()
