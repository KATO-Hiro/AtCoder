# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = float("inf")

    if n == 1:
        print(1)
        exit()

    for b in range(62):
        a_lower = 0
        a_upper = n

        while (a_upper - a_lower) > 1:
            a = (a_lower + a_upper) // 2
            c = n - a * (2 ** b)

            if c >= 0:
                a_lower = a

                ans = min(ans, a + b + c)
            else:
                a_upper = a

    print(ans)


if __name__ == "__main__":
    main()
