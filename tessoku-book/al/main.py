# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    d, n = map(int, input().split())
    a = [24] * 366

    for _ in range(n):
        li, ri, hi = map(int, input().split())

        for day in range(li, ri + 1):
            a[day] = min(a[day], hi)

    ans = 0
    
    for day in range(1, d + 1):
        ans += a[day]
    
    print(ans)


if __name__ == "__main__":
    main()
