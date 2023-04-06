# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = [list(input().rstrip()) for _ in range(8)]

    for i in range(7, -1, -1):
        for j in range(8):
            if s[i][j] == "*":
                print(f"{'abcdefgh'[j]}{8 - i}")
                exit()
    

if __name__ == "__main__":
    main()
