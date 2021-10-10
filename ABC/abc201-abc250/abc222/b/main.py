# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0

    for ai in a:
        if ai < p:
            count += 1
    
    print(count)


if __name__ == "__main__":
    main()
