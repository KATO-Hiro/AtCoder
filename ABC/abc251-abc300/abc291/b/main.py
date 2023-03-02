# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    x = sorted(list(map(int, input().split())))
    y = x[n:-n]
    print(sum(y) / (3 * n))
    

if __name__ == "__main__":
    main()
