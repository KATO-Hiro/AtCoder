# -*- coding: utf-8 -*-


def main():
    n = int(input())
    high_score = 0

    for i in range(n):
        a, b, c, d, e = list(map(int, input().split()))
        current_score = a + b + c + d + (110 / 900) * e
        high_score = max(current_score, high_score)

    print(high_score)


if __name__ == '__main__':
    main()
