# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    p = [0] + list(map(int, input().split()))
    q = [0] + list(map(int, input().split()))
    r = [0] + list(map(int, input().split()))
    d = defaultdict(float)

    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                d[i + j + k] += p[i] * q[j] * r[k] / (10 ** 6)

    for i in range(1, 19):
        print(d[i])
    

if __name__ == "__main__":
    main()
