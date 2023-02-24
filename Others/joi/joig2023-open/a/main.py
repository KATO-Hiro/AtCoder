# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()

    if s[-1] == "G":
        print(s[:-1])
    else:
        print(s + "G")
    

if __name__ == "__main__":
    main()
