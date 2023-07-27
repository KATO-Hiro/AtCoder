# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    c = list()

    # xiとyjの共通する要素がない場合のaiの最大値
    # See:
    # https://note.nkmk.me/python-set/#intersection
    for i in range(n):
        _ = int(input())
        xi = set(map(int, input().split()))
        c.append((a[i], i + 1, xi))

    c = sorted(c, reverse=True)

    q = int(input())

    for _ in range(q):
        _ = int(input())
        yj = set(map(int, input().split()))
        ans = -1

        for _, i, xi in c:
            if yj.isdisjoint(xi):
                ans = i
                break

        print(ans)


if __name__ == "__main__":
    main()
