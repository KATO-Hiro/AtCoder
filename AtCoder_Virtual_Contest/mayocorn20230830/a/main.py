# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, d = map(int, input().split())
    s = [input().rstrip() for _ in range(n)]
    ans = 0
    count = 0

    for j in range(d):
        ok = True

        for i in range(n):
            if s[i][j] == "x":
                ok = False
                break

        if ok:
            count += 1
        else:
            count = 0

        ans = max(ans, count)

    print(ans)


if __name__ == "__main__":
    main()
