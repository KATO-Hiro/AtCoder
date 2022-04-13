# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0

    if a[0] > x:
        count += a[0] - x
        a[0] -= count

    for i in range(n - 1):
        diff = a[i] + a[i + 1] - x

        if diff > 0:
            count += diff
            a[i + 1] -= diff
    
    print(count)


if __name__ == "__main__":
    main()
