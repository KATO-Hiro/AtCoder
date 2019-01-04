# -*- coding: utf-8 -*-


def main():
    abcd = sorted([int(input()) for _ in range(4)])
    ef = sorted([int(input()) for _ in range(2)])
    print(sum(abcd[1:] + ef[1:]))


if __name__ == '__main__':
    main()
