# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline
    
    n = int(input())
    a = [0] * n
    b = [0] * n
    c = [0.0] * n
    t = 0.0
    
    for i in range(n):
        ai, bi = map(int, input().split())
        a[i] = ai
        b[i] = bi
        c[i] = ai / bi
        t += c[i]
    
    remain = t / 2
    ans = 0.0
    
    for i in range(n):
        if remain < 0.0:
            continue

        if remain - c[i] >= 0:
            ans += a[i]
        else:
            ans += remain * b[i]

        remain -= c[i]

    print(ans)


if __name__ == "__main__":
    main()
