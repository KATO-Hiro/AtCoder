# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    w, l = [], []

    for _ in range(n):
        wi, li = map(int, input().split())
        w.append(wi)
        l.append(li)

    for _ in range(m):
        pi, ci = map(int, input().split())
        pi -= 1

        w[pi] += ci

    ans = 0

    for wj, lj in zip(w, l):
        if wj > lj:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
