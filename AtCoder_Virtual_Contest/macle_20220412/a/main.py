# -*- coding: utf-8 -*-


def main():
    from itertools import product
    import sys

    input = sys.stdin.readline

    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = 0

    for pattern in product([0, 1], repeat=n):
        values = 0
        costs = 0

        for i, (vi, ci) in enumerate(zip(v, c)):
            if pattern[i] == 1:
                values += vi
                costs += ci
        
        ans = max(ans, values - costs)
    
    print(ans)


if __name__ == "__main__":
    main()
