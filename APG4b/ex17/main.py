# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))
    ans = 0

    for ai in a:
        for pi in p:
            if (ai + pi) == s:
                ans += 1
    
    print(ans)


if __name__ == "__main__":
    main()
