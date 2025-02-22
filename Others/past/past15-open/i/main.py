# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    size = max(a) + 1
    b = [0] * size
    c = [0] * size

    for ai in a:
        b[ai] += 1

    for number in range(1, size):
        for d in range(number, size, number):
            c[number] += b[d]

    ans = 1

    for number in range(1, size):
        if c[number] < k:
            continue

        ans = max(ans, number)

    print(ans)


if __name__ == "__main__":
    main()
