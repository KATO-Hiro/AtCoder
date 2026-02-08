# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    size_max = 3 * 10**5
    b = [0] * size_max

    for ai in a:
        b[0] += 1
        b[ai] -= 1

    b = list(accumulate(b))

    for i in range(size_max - 1):
        if b[i] < 10:
            continue

        p, q = divmod(b[i], 10)
        b[i + 1] += p
        b[i] = q

    while b and b[-1] == 0:
        b.pop()

    b = b[::-1]
    print("".join(map(str, b)))


if __name__ == "__main__":
    main()
