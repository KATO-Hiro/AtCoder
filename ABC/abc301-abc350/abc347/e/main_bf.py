# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    x = list(map(int, input().split()))
    s = set()
    size = 0
    a = [0] * (n + 1)

    for xi in x:
        if xi in s:
            s.discard(xi)
            size -= 1
        else:
            s.add(xi)
            size += 1

        for sj in s:
            a[sj] += size

    print(*a[1:])


if __name__ == "__main__":
    main()
