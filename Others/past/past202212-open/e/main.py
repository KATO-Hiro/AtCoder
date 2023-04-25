# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    count = 0

    for si in s:
        if si == "(":
            count += 1
        else:
            if count > 0:
                count -= 1
            else:
                print("No")
                exit()
    
    if count == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
