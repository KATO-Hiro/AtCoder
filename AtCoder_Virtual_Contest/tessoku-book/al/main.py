# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    d, n = map(int, input().split())
    work_hours = [24] * (d + 1)
    work_hours[0] = 0

    for _ in range(n):
        li, ri, hi = map(int, input().split())

        for day in range(li, ri + 1):
            work_hours[day] = min(work_hours[day], hi)

    print(sum(work_hours))


if __name__ == "__main__":
    main()
