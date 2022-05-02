# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ab = list()
    t = 0

    for i in range(n):
        ai, bi = map(int, input().split())
        ab.append((ai, bi, ai / bi))
        t += ai / bi
    
    time = 0
    ans = 0

    for ai, bi, ai_bi in ab:
        if time + ai_bi <= t / 2:
            time += ai_bi
            ans += ai
        else:
            ans += (t / 2 - time) * bi
            print(ans)
            exit()


if __name__ == "__main__":
    main()
