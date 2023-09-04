# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    p = list(map(lambda x: int(x) + 1, input().split()))
    # print(p)
    summed = sum(p[:k])
    ans = summed

    for i in range(k, n):
        summed += p[i]
        summed -= p[i - k]
        ans = max(ans, summed)

    print(ans / 2)


if __name__ == "__main__":
    main()
