# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline
    
    c = list(input().rstrip())

    if len(set(c)) == 1:
        print("Won")
    else:
        print("Lost")


if __name__ == "__main__":
    main()
