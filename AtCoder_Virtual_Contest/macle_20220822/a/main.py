# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    t = "oxx" * 10
    s = input().rstrip()
    n = len(s)

    for i in range(3):
        if t[i:i + n] == s:
            print("Yes")
            exit()
    
    print("No")


if __name__ == "__main__":
    main()
