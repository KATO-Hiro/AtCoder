# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = [list(input().rstrip()) for _ in range(n)]
    b = [list(input().rstrip()) for _ in range(m)]

    for i in range(n - m + 1):
        for j in range(n - m + 1):
            flag = True

            for k in range(i, i + m):
                for l in range(j, j + m):
                    if a[k][l] != b[k - i][l - j]:
                        flag = False
                        break

            if flag:
                print("Yes")
                exit()

    print("No")


if __name__ == "__main__":
    main()
