# -*- coding: utf-8 -*-


def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    count = 0

    for hi in h:
        if hi >= k:
            count += 1

    print(count)


if __name__ == '__main__':
    main()
