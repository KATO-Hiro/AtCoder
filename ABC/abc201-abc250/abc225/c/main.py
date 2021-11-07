# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        for j in range(m):
            b[i][j] -= 1
    
    p, q = divmod(b[0][0], 7)
   
    if (q + m - 1) >= 7:
        print("No")
        exit()

    for i in range(n):
        for j in range(m):
            next_bij = (p + i) * 7 + (q + j)

            if next_bij != b[i][j]:
                print("No")
                exit()

    print("Yes")


if __name__ == "__main__":
    main()
