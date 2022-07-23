# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = [list(input().rstrip()) for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            flag = False

            if a[i][j] == 'W' and a[j][i] == "L":
                flag = True
            if a[i][j] == 'L' and a[j][i] == "W":
                flag = True
            if a[i][j] == 'D' and a[j][i] == "D":
                flag = True

            if not flag:
                print("incorrect")
                exit()
    
    print("correct")


if __name__ == "__main__":
    main()
