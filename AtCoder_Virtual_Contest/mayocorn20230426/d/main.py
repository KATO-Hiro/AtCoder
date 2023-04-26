# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n = int(input())
    d = defaultdict(int)
    
    for _ in range(n):
        ai, bi = map(int, input().split())
        d[ai] += 1
        d[ai + bi] -= 1
    
    days = sorted(d.keys())
    ans = [0] * (n + 1)
    prev_day, people_count = 0, 0

    for day in days:
        ans[people_count] += day - prev_day
        people_count += d[day]
        prev_day = day
    
    print(*ans[1:])


if __name__ == "__main__":
    main()
