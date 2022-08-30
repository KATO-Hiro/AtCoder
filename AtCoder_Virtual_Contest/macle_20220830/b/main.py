# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = [input().rstrip() for _ in range(n)]

    # 横
    for i in range(n):
        for j in range(n):
            count = 0

            for k in range(6):
                if j + k >= n:
                    count = -1
                    continue

                if s[i][j + k] == "#":
                    count += 1
            
            if count >= 4:
                print("Yes")
                exit()

    # 縦
    for j in range(n):
        for i in range(n):
            count = 0

            for k in range(6):
                if i + k >= n:
                    count = -1
                    continue

                if s[i + k][j] == "#":
                    count += 1
            
            if count >= 4:
                print("Yes")
                exit()

    # 左上から右下
    for i in range(n):
        for j in range(n):
            count = 0

            for k in range(6):
                if i + k >= n or j + k >= n:
                    count = -1
                    continue

                if s[i + k][j + k] == "#":
                    count += 1
        
            if count >= 4:
                print("Yes")
                exit()

    # 右上から左下
    for i in range(n):
        for j in range(n - 1, -1, -1):
            count = 0

            for k in range(6):
                if i + k >= n or j - k < 0:
                    count = -1
                    continue

                if s[i + k][j - k] == "#":
                    count += 1
        
            if count >= 4:
                print("Yes")
                exit()


    print("No")


if __name__ == "__main__":
    main()
