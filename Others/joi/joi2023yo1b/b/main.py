# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a = int(input())
    b = int(input())

    if a < b:
        print(-1)
    elif a == b:
        print(0)
    else:
        print(1)
   

if __name__ == "__main__":
    main()
