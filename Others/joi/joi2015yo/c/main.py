# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(h)]
    ans = [[-1 for _ in range(w)] for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if s[i][j] == "c":
                ans[i][j] = 0
            elif j >= 1 and ans[i][j - 1] != -1:
                ans[i][j] = ans[i][j - 1] + 1

    for ans_i in ans:
        print(*ans_i)


if __name__ == "__main__":
    main()
