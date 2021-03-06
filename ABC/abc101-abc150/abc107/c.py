# -*- coding: utf-8 -*-


def main():
    n, k = list(map(int, input().split()))
    x = list(map(int, input().split()))
    ans = float('inf')

    for i in range(n - k + 1):
        left = x[i]
        right = x[i + k - 1]
        abs_left = abs(left)
        abs_right = abs(right)

        if left * right >= 0:
            ans = min(ans, max(abs_left, abs_right))
        else:
            ans = min(ans, 2 * abs_left + abs_right, abs_left + 2 * abs_right)

    print(ans)


if __name__ == '__main__':
    main()
