# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    c = list()

    # xiとyjの積集合を取り、共通する要素が0個となるaiの最大値
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
            if len(yj & xi) == 0:
                ans = i
                break

        print(ans)


if __name__ == "__main__":
    main()
