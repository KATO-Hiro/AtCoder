# -*- coding: utf-8 -*-


def main():
    p, q, r = map(int, input().split())
    print(p + q + r - max(p, q, r))


if __name__ == '__main__':
    main()
