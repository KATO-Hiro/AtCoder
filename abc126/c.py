# -*- coding: utf-8 -*-


def main():
    n, k = map(int, input().split())
    ans = 0

    for i in range(1, n + 1):
        if i >= k:
            ans += 1
        else:
            m = 1

            while i * 2 ** m < k:
                m += 1

            ans += (1 / 2) ** m

    print(ans / n)


if __name__ == '__main__':
    main()
