# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    import sys

    input = sys.stdin.readline

    d = int(input())
    n = int(input())
    count = [0] * (d + 10)

    for _ in range(n):
        li, ri = map(int, input().split())
        count[li] += 1
        count[ri + 1] -= 1
    
    imos = list(accumulate(count))

    for i in range(1, d + 1):
        print(imos[i])
    

if __name__ == "__main__":
    main()
