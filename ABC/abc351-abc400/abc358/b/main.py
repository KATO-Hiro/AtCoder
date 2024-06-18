# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, a = map(int, input().split())
    t = list(map(int, input().split()))
    prev = 0
    ans = list()

    for ti in t:
        if ti >= prev:
            u = ti + a
            ans.append(u)
            prev = u
        else:
            prev += a
            ans.append(prev)

    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()
