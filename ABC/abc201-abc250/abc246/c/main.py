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

        used = min(p, k)
        ai -= used * x
        k -= used

        r.append(ai)
    
    for ri in sorted(r, reverse=True):
        if k > 0:
            k -= 1
        else:
            ans += ri

    print(ans)


if __name__ == "__main__":
    main()
