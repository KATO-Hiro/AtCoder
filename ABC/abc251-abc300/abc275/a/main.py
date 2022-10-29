# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    h = list(map(int, input().split()))
    hj = 0
    ans = 0

    for i, hi in enumerate(h, 1):
        if hi > hj:
            ans = i
            hj = hi
    
    print(ans)
    

if __name__ == "__main__":
    main()
