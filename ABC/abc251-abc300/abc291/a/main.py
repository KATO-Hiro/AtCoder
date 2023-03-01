# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()

    for i, si in enumerate(s, 1):
        if si.isupper():
            print(i)
            exit()
    

if __name__ == "__main__":
    main()
