# -*- coding: utf-8 -*-


def main():
    n = int(input())
    p, q = divmod(n - 1, 9)

    # See:
    # https://www.slideshare.net/chokudai/arc046
    result = [q + 1] * (p + 1)
    print(''.join(map(str, result)))


if __name__ == '__main__':
    main()
