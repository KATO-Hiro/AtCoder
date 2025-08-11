# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    x = [1]
    pos, remain, summed = 0, n, 1

    for ai in a:
        while pos < ai:
            summed += remain
            x.append(summed)
            pos += 1

        remain -= 1

    x.pop()
    size = len(x)

    for _ in range(q):
        bj = int(input())
        bj -= 1

        if bj < size:
            print(x[bj])
        else:
            print(-1)


if __name__ == "__main__":
    main()
