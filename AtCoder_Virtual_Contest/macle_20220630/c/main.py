# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = Counter(a)

    for i in range(m):
        bi, ci  = map(int, input().split())
        c[ci] += bi
    
    ans = 0
    
    for value in sorted(c.keys(), reverse=True):
        count = c[value]
        need = min(n, count)
        n -= need
        ans += need * value

        if n == 0:
            print(ans)
            exit()


if __name__ == "__main__":
    main()
