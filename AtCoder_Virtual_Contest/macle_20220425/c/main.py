# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = float("inf")

    for bit in range(1 << (n - 1)):
        candidate = 0
        inner = 0

        for j in range(n):
            inner |= a[j]

            if bit >> j & 1:
                candidate ^= inner
                inner = 0
        
        candidate ^= inner
        ans = min(ans, candidate)
    
    print(ans)


if __name__ == "__main__":
    main()
