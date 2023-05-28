# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    # 標準化
    s = input().rstrip().replace("1", "l").replace("0", "o")
    t = input().rstrip().replace("1", "l").replace("0", "o")

    if s == t:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
