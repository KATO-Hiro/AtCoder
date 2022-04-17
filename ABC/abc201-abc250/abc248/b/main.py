# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, k = map(int, input().split())
    count = 0

    while True:
        if a >= b:
            print(count)
            exit()
        
        count += 1
        a *= k


if __name__ == "__main__":
    main()
