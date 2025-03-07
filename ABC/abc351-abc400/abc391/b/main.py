# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(n)]
    t = [list(input().rstrip()) for _ in range(m)]

    for a in range(n - m + 1):
        for b in range(n - m + 1):
            ok = True

            for i in range(m):
                for j in range(m):
                    ni, nj = a + i, b + j

                    if not (0 <= ni < n):
                        ok = False
                        break
                    if not (0 <= nj < n):
                        ok = False
                        break
                    if s[ni][nj] != t[i][j]:
                        ok = False
                        break

            if ok:
                print(a + 1, b + 1)
                exit()


if __name__ == "__main__":
    main()
