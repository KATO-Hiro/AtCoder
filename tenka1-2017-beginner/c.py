# -*- coding: utf-8 -*-


def main():
    large_n = int(input())

    for h in range(1, 3500 + 1):
        for n in range(1, 3500 + 1):
            a = large_n * h * n
            b = 4 * h * n - large_n * (n + h)

            if b != 0:
                w, q = divmod(a, b)

                if q == 0 and w > 0:
                    print(h, n, w)
                    exit()


if __name__ == '__main__':
    main()
