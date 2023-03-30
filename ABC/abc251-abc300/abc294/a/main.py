# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = list()

    for ai in a:
        if ai % 2 == 0:
            ans.append(ai)
    
    print(*ans)
    

if __name__ == "__main__":
    main()
