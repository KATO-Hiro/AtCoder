# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    x = list(map(int, input().split()))
    ans = float("inf")

    for p in range(-210, 210):
        summed = 0

        for xi in x:
            summed += (xi - p) ** 2
        
        ans = min(ans, summed)

    print(ans)


if __name__ == "__main__":
    main()
