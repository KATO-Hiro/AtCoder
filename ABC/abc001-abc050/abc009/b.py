# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    print(sorted(set(a), reverse=True)[1])


if __name__ == '__main__':
    main()
