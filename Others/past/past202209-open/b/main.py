# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = input().rstrip()

    if len(n) <= 2:
        print(0)
    else:
        print(n[:-2])
    

if __name__ == "__main__":
    main()
