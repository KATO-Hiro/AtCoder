# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))

    for _ in range(n - 1):
        b = list()

        for ai, aj in zip(a, a[1:]):
            b.append(abs(ai - aj))

        a = b
    
    print(*a)
    

if __name__ == "__main__":
    main()
