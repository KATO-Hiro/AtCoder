# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate

    while True:
        n, k = map(int, input().split())

        if n == 0 and k == 0:
            exit()

        x = list(accumulate([0] + sorted(list(map(int, input().split())))))
        print(x[k])


if __name__ == "__main__":
    main()
