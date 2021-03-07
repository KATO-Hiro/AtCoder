# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    pos = [[] for _ in range(n)]

    for index, ai in enumerate(a):
        pos[ai].append(index)

    for i in range(n):
        prev = -1
        pos[i].append(n)

        for p in pos[i]:
            if p - prev > m:
                print(i)
                exit()

            prev = p

    print(n)


if __name__ == "__main__":
    main()
