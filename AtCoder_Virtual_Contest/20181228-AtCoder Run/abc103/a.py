# -*- coding: utf-8 -*-


def main():
    a = list(map(int, input().split()))
    print(max(a) - min(a))


if __name__ == '__main__':
    main()
