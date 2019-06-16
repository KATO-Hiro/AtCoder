# -*- coding: utf-8 -*-


def main():
    from bisect import bisect

    n, x = map(int, input().split())
    ls = list(map(int, input().split()))
    dist = [0]

    for i in range(1, n + 1):
        dist.append(dist[i - 1] + ls[i - 1])

    print(bisect(dist, x))


if __name__ == '__main__':
    main()
