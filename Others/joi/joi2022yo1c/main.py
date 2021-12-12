# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = int(input())
    a = int(input())
    b = int(input())
    ans = 250
    height = a
    
    while height < s:
        height += b
        ans += 100
    
    print(ans)


if __name__ == "__main__":
    main()
