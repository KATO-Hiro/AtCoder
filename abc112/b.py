# -*- coding: utf-8 -*-


def main():
    n, large_t = map(int, input().split())
    cost = 10000
    count = 0

    for i in range(n):
        ci, ti = map(int, input().split())

        if ti <= large_t:
            cost = min(cost, ci)
        else:
            count += 1

    if count != n:
        print(cost)
    else:
        print('TLE')


if __name__ == '__main__':
    main()
