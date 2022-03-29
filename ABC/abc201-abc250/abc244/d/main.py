# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip().split()
    t = input().rstrip().split()
    count = 0

    for si, ti in zip(s, t):
        if si == ti:
            count += 1
    
    if count == 0 or count == 3:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
