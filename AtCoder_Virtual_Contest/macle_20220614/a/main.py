# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    o = input().rstrip()
    t = input().rstrip()
    n = len(o)
    m = len(t)
    ans = ""

    for oi, ti in zip(o, t):
        ans += oi
        ans += ti
    
    if n > m:
        ans += o[-1]
    
    print(ans)


if __name__ == "__main__":
    main()
