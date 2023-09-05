# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))

    candidate = sum(a[::2]) - sum(a[1::2])
    # print(candidate)
    ans = [candidate]

    for i in range(1, n):
        candidate = 2 * a[i - 1] - ans[-1]
        ans.append(candidate)

    print(*ans)


if __name__ == "__main__":
    main()
