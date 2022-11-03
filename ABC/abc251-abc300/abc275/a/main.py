# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    h = list(map(int, input().split()))
    ans = sorted({(hi, i) for i, hi in enumerate(h, 1)})
    print(ans[-1][1])
    

if __name__ == "__main__":
    main()
