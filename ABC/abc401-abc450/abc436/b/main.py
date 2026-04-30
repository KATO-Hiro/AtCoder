# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    pending = -1
    ans = [[pending for _ in range(n)] for _ in range(n)]
    r, c, k = 0, (n - 1) // 2, 1
    ans[r][c] = k

    while k < n**2:
        k += 1

        nr, nc = (r - 1) % n, (c + 1) % n

        if ans[nr][nc] != pending:
            nr, nc = (r + 1) % n, c

        ans[nr][nc] = k
        r, c = nr, nc

    for ans_i in ans:
        print(*ans_i)


if __name__ == "__main__":
    main()
