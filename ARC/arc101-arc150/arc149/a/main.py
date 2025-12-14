# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline
    sys.set_int_max_str_digits(0)

    n, m = map(int, input().split())
    pending = -1
    ans = [pending]

    for base in range(1, 10):
        number = base
        candidate = pending

        for digit in range(1, n + 1):
            if number % m == 0:
                candidate = str(base) * digit

            number *= 10
            number += base
            number %= m

        if candidate == pending:
            continue

        ans += [int(candidate)]

    ans.sort()
    print(ans[-1])


if __name__ == "__main__":
    main()
