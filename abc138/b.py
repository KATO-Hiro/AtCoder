# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    total = 0

    for ai in a:
        total += 1 / ai

    print(1 / total)


if __name__ == '__main__':
    main()
