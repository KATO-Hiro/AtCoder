# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k, x = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse=True)
    r = list()
    ans = 0

    for ai in a:
        p, q = divmod(ai, x)

        if k > 0:
            if k >= p:
                k -= p
            else:
                ans += (p - k) * x
                k = 0
        else:
            ans += p * x

        r.append(q)
    
    for ri in sorted(r, reverse=True):
        if k > 0:
            k -= 1
        else:
            ans += ri

    print(ans)


if __name__ == "__main__":
    main()
