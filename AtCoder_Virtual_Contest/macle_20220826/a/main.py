# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = list()

    for ai in a:
        if ai == x:
            continue
    
        ans.append(ai)
    
    print(*ans)


if __name__ == "__main__":
    main()
