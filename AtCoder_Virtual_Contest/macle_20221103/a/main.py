# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = list(input().rstrip())
    t = list(input().rstrip())
    diff_count = 0

    for si, ti in zip(s, t):
        if si != ti:
            diff_count += 1
    
    if diff_count == 2:
        print("No")
    else:
        print("Yes")



if __name__ == "__main__":
    main()
