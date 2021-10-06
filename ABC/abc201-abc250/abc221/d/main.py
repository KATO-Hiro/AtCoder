# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n = int(input())
    status = defaultdict(int)
    
    for _ in range(n):
        ai, bi = map(int, input().split())
        status[ai] += 1
        status[ai + bi] -= 1
    
    days = sorted(status.keys())
    prev = 0
    cur = 0
    ans = [0] * (n + 1)

    for day in days:
        ans[cur] += day - prev
        cur += status[day]
        prev = day

    print(*ans[1:])


if __name__ == "__main__":
    main()
