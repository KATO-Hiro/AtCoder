# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    t = [
        "###.?????",
        "###.?????",
        "###.?????",
        "....?????",
        "?????????",
        "?????....",
        "?????.###",
        "?????.###",
        "?????.###",
    ]

    n, m = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(n)]
    ans = list()

    for i in range(n):
        if i + 9 > n:
            continue

        for j in range(m):
            if j + 9 > m:
                continue

            flag = True
            # print(i, j)

            for y in range(9):
                for x in range(9):
                    if t[y][x] == "?":
                        continue

                    if s[i + y][j + x] != t[y][x]:
                        flag = False
                        break

            # print(i, j, flag)
            if flag:
                ans.append((i + 1, j + 1))

    # print(ans)

    for i, j in sorted(ans):
        print(i, j)


if __name__ == "__main__":
    main()
