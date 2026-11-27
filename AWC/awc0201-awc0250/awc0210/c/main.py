# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    size = 0
    b = []

    for ai in a:
        if ai < x:
            break
        if size == k:
            break

        b.append(ai)
        size += 1

    if len(b) != k:
        print(-1)
    else:
        print("".join(map(str, b)))


if __name__ == "__main__":
    main()
