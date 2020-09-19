# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = [int(input()) for _ in range(n)]
    b = [int(input()) for _ in range(m)]
    vote_count = [0 for _ in range(n)]

    for bj in b:
        for index, ai in enumerate(a):
            if bj >= ai:
                vote_count[index] += 1
                break

    vote_max = max(vote_count)

    for index, count in enumerate(vote_count, 1):
        if count == vote_max:
            print(index)
            exit()


if __name__ == '__main__':
    main()
