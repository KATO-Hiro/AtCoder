# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0

    for ai, bi in zip(a, b):
        ans += min(ai, bi)

    for _ in range(q):
        ci, *args = map(str, input().split())
        xi, vi = map(int, args)
        xi -= 1

        # 初期解との差分ではなく、直前との差分を取る
        ans -= min(a[xi], b[xi])

        if ci == "A":
            a[xi] = vi
        else:
            b[xi] = vi

        ans += min(a[xi], b[xi])

        print(ans)


if __name__ == "__main__":
    main()
