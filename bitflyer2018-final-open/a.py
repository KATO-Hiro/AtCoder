# -*- coding: utf-8 -*-


def count_digit(number):
    if number % 10 != 0:
        return 0

    return count_digit(number // 10) + 1


if __name__ == '__main__':
    n = int(input())
    p = [int(input()) for _ in range(n)]
    ans = [0 for _ in range(n)]
    i = 0

    for pi in p:
        ans[i] = count_digit(pi)
        i += 1

    print(min(ans))
