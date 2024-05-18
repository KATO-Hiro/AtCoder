# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    sc = sorted([tuple(map(str, input().rstrip().split())) for _ in range(n)])
    r_sum = 0

    for i in range(n):
        r_sum += int(sc[i][1])

    id = r_sum % n
    print(sc[id][0])


if __name__ == "__main__":
    main()
