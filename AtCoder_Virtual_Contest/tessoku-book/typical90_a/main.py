# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, l = map(int, input().split())
    k = int(input())
    a = [0] + list(map(int, input().split())) + [l]
    pieces = [ai - aj for ai, aj in zip(a[1:], a)]
    left = 0
    right = 10**9 + 1

    def f(size_min):
        count = 0
        summed = 0

        for piece in pieces:
            if summed + piece >= size_min:
                count += 1
                summed = 0
            else:
                summed += piece

        return count

    while right - left > 1:
        mid = (left + right) // 2

        if f(mid) >= k + 1:
            left = mid
        else:
            right = mid

    print(left)


if __name__ == "__main__":
    main()
