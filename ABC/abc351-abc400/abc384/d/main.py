# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    summed_a = sum(a)
    b = a + a
    n *= 2
    _, q = divmod(s, summed_a)

    right = 0
    summed = 0

    for left in range(n):
        while right < n and summed + b[right] <= q:
            summed += b[right]
            right += 1

        if summed == q:
            print("Yes")
            exit()

        summed -= b[left]

        if right < left:
            right = left

    print("No")


if __name__ == "__main__":
    main()
