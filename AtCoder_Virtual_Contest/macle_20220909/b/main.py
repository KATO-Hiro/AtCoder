# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    all = 0

    for ai in a:
        all ^= ai
    
    ans = list()

    for ai in a:
        ans.append(all ^ ai)
    
    print(*ans)


if __name__ == "__main__":
    main()
