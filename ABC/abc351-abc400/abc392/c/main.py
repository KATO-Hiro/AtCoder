# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    size = 3 * 10**5 + 10
    numbers = [-1] * size

    for i, qi in enumerate(q):
        numbers[qi] = i

    ans = list()

    for i in range(1, n + 1):
        ni = numbers[i]
        pi = p[ni]
        si = q[pi - 1]
        ans.append(si)

    print(*ans)


if __name__ == "__main__":
    main()
