# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline
    x = list(input().rstrip())
    n = len(x)
    digit_sum = sum([int(xi) for xi in x])
    xi = 0
    ans = ''

    for i in range(n - 1, -1, -1):
        xi += digit_sum
        digit_sum -= int(x[i])

        p, q = divmod(xi, 10)
        ans += str(q)
        xi = p

    # 繰り上がりの処理
    while xi > 0:
        pi, qi = divmod(xi, 10)
        ans += str(qi)
        xi = pi

    print(ans[::-1])


if __name__ == "__main__":
    main()
