# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    w = input().rstrip().split()
    count = 0

    for i in range(k):
        if w[i] != "S":
            continue

        count += 1

    ans = count

    for i in range(k, n):
        if w[i] == "S":
            count += 1
        if w[i - k] == "S":
            count -= 1

        ans = max(ans, count)

    print(ans)


if __name__ == "__main__":
    main()
