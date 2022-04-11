# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    index = 1
    ans = 0

    for ai in a:
        if ai == index:
            index += 1
        else:
            ans += 1
    
    if ans == n:
        ans = -1
    
    print(ans)


if __name__ == "__main__":
    main()
