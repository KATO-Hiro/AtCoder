# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, c = map(int, input().split())
    n = int(input())
    ok = set()
    ng = set()
    ans = [2] * (a + b + c)

    for _ in range(n):
        i, j, k, ri = map(int, input().split())
        i -= 1
        j -= 1
        k -= 1

        if ri == 1:
            ok.add((i, j, k))
            ans[i] = ans[j] = ans[k] = 1
        else:
            ng.add((i, j, k))

    for i, j, k in ng:
        ai, aj, ak = ans[i], ans[j], ans[k]

        if ai == aj == 1 and ak == 2:
            ans[k] = 0
        elif aj == ak == 1 and ai == 2:
            ans[i] = 0
        elif ai == ak == 1 and aj == 2:
            ans[j] = 0

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
