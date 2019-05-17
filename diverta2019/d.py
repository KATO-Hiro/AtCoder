# -*- coding: utf-8 -*-


def main():
    n = int(input())
    ans = 0

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0 and (i ** 2) != n:
            m = n // i - 1

            if n // m == n % m:
                ans += m

    print(ans)


if __name__ == '__main__':
    main()
