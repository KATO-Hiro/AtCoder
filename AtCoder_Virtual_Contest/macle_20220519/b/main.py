# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    x = 0

    for ai in a:
        x ^= ai

    ans = list()

    for ai in a:
        ans.append(x ^ ai)
    
    print(*ans)


if __name__ == "__main__":
    main()
