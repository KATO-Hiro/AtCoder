# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x = map(int, input().split())
    x *= 100
    summed = 0

    for i in range(n):
        vi, pi = map(int, input().split())
        summed += vi * pi

        if summed > x:
            print(i + 1)
            exit()
    
    print(-1)


if __name__ == "__main__":
    main()
