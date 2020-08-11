# -*- coding: utf-8 -*-


def main():
    n, l = map(int, input().split())
    taste = [l + i for i in range(n)]
    total = sum(taste)
    value_min = min(taste)
    value_max = max(taste)

    if value_min > 0:
        print(total - value_min)
    elif 0 in taste:
        print(total)
    elif value_max < 0:
        print(total - value_max)


if __name__ == '__main__':
    main()
