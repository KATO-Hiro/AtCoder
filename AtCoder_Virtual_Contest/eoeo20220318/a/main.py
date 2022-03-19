# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    w = list(map(int, input().split()))
    ans = float('inf')

    for i in range(1, n):
        s1 = sum(w[:i])
        s2 = sum(w[i:])
        ans = min(ans, abs(s1 - s2))
    
    print(ans)


if __name__ == "__main__":
    main()
