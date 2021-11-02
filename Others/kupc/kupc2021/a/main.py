# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = sorted(list(map(int, input().split())))
    t = int(input())
    prev = -1
    ans = 0

    for si in s:
        p, q = divmod(si, t)
        
        if p != prev:
            prev = p
            ans += 1
    
    print(ans)


if __name__ == "__main__":
    main()
