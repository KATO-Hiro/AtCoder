# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    h = list(map(int, input().split()))
    prev = h[0]
    count = 0
    ans = 0

    for hi in h[1:]:
        if hi <= prev:
            count += 1
        else:
            count = 0
        
        prev = hi
        ans = max(ans, count)
    
    print(ans)


if __name__ == "__main__":
    main()
