# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    x = list(map(int, input().split()))
    dist_max = 201
    ans = float("inf")

    for p in range(-dist_max, dist_max + 1):
        candidate = 0

        for xi in x:
            candidate += (xi - p) ** 2
        
        ans = min(ans, candidate)
    
    print(ans)


if __name__ == "__main__":
    main()
