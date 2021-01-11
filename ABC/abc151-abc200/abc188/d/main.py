# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, large_c = map(int, input().split())
    events = list()

    for i in range(n):
        ai, bi, ci = map(int, input().split())

        events.append((ai, ci))
        events.append((bi + 1, -ci))

    prev_day = 0
    summed = 0
    ans = 0

    for event in sorted(events):
        now_day = event[0]
        cost = event[1]

        ans += min(large_c, summed) * (now_day - prev_day)
        summed += cost
        prev_day = now_day

    print(ans)


if __name__ == "__main__":
    main()
