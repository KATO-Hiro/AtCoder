# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w, q = map(int, input().split())
    ans = [[0 for _ in range(w)] for _ in range(h)]
    covered = [[False for _ in range(w)] for _ in range(h)]

    for _ in range(q):
        query, *others = map(int, input().split())

        if query == 1:
            yk, xk, ck = others
            yk -= 1
            xk -= 1

            for ny in range(yk, yk + 1 + 1):
                for nx in range(xk, xk + 1 + 1):
                    if covered[ny][nx]:
                        continue

                    ans[ny][nx] = ck
        else:
            yk, xk = others
            yk -= 1
            xk -= 1

            for ny in range(yk, yk + 1 + 1):
                for nx in range(xk, xk + 1 + 1):
                    covered[ny][nx] = True

    for ans_i in ans:
        print(*ans_i)


if __name__ == "__main__":
    main()
