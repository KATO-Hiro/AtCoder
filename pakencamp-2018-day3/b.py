# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    count = 0
    years = 0

    for ai in a:
        years += ai

        if years <= 2018:
            count += 1

    print(count)


if __name__ == '__main__':
    main()
