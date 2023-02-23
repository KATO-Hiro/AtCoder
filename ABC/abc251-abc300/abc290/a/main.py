# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0

    for bi in b:
        ans += a[bi - 1]
    
    print(ans)
    

if __name__ == "__main__":
    main()
