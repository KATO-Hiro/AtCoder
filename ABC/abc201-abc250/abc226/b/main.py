# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = set()

    for i in range(n):
        line = tuple(map(int, input().split()))
        s.add(line)
    
    print(len(s))


if __name__ == "__main__":
    main()
