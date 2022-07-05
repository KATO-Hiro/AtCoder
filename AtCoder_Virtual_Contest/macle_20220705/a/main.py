# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = 0
    pre = -100

    for ai in a:
        ai -= 1

        ans += b[ai]

        if pre + 1 == ai:
            ans += c[ai - 1]
        
        pre = ai
    
    print(ans)


if __name__ == "__main__":
    main()
