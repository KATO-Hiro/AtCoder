# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    count = 1

    for i in range(1, n + 1):
        count *= i
    
    print(count)


if __name__ == "__main__":
    main()
