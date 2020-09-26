# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    abc = sorted(map(int, input().split()))
    print(abc[1])


if __name__ == '__main__':
    main()
