# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = sum(a)
    a = a + a
    left = 0
    summed = 0

    for right, ai in enumerate(a):
        summed += ai

        while left < n + 1 and summed * 10 > b:
            summed -= a[left]
            left += 1

        if summed * 10 == b:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
