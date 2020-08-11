# -*- coding: utf-8 -*-


def main():
    a, b = input().split()
    a_max = max(int(a), int('9' + a[1:]), int(a[0] + '9' + a[2]), int(a[:2] + '9'))
    b_min = min(int(b), int('1' + b[1:]), int(b[0] + '0' + b[2]), int(b[:2] + '0'))
    print(max(int(a) - b_min, a_max - int(b)))


if __name__ == '__main__':
    main()
