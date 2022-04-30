# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = Counter(a)

    for i in range(m):
        bi, ci = map(int, input().split())
        c[ci] += bi
    
    numbers = sorted(c.items(), key=lambda x: x[0], reverse=True)
    ans = 0
    remain = n

    for number, count in numbers:
        candidate = min(remain, count)
        ans += number * candidate
        remain -= candidate

        if remain == 0:
            print(ans)
            exit()


if __name__ == "__main__":
    main()
