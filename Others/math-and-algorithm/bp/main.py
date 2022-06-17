# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    left = 0
    right = 0

    for si in s:
        if si == "(":
            left += 1
        else:
            right += 1
        
        if right > left:
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
