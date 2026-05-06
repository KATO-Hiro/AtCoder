# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(h)]
    k = 0
    ans = []

    for i in range(h):
        for j in range(w):
            if s[i][j] == "T":
                ans.append((i + 1, j + 1))
                k += 1

    print(k)

    for ri, ci in ans:
        print(ri, ci)


if __name__ == "__main__":
    main()
