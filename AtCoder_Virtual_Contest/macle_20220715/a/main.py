# -*- coding: utf-8 -*-


def digit_sum(number):
    total = 0

    while number > 0:
        total += number % 10
        number //= 10
    
    return total


def main():
    import sys

    input = sys.stdin.readline

    n, a, b = map(int, input().split())
    ans = 0

    for i in range(1, n + 1):
        summed = digit_sum(i)

        if a <= summed <= b:
            ans += i
    
    print(ans)


if __name__ == "__main__":
    main()
