# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline
    
    s = input().rstrip()
    print('0' + s[:3])


if __name__ == "__main__":
    main()
