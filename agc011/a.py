# -*- coding: utf-8 -*-


def main():
    n, c, k = list(map(int, input().split()))
    t = sorted([int(input()) for _ in range(n)])

    remain_seats = c - 1
    departure_time = t[0] + k
    bus_count = 1

    # See:
    # https://www.youtube.com/watch?v=cJ-WjtA34GQ
    for i in range(1, n):
        if remain_seats >= 1 and t[i] <= departure_time:
            remain_seats -= 1
        else:
            bus_count += 1
            remain_seats = c - 1
            departure_time = t[i] + k

    print(bus_count)


if __name__ == '__main__':
    main()
