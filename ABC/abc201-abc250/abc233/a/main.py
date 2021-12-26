# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x, y = map(int, input().split())
    total = x
    count = 0

    while total < y:
        total += 10
        count += 1
    
    print(count)


if __name__ == "__main__":
    main()
