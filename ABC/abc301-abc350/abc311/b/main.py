# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, d = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(n)]
    ans = 0
    candidate = 0

    for j in range(d):
        ok = True

        for i in range(n):
            if s[i][j] != "o":
                ok = False
                break

        if ok:
            candidate += 1
        else:
            candidate = 0

        ans = max(ans, candidate)

    print(ans)


if __name__ == "__main__":
    main()
