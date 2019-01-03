# -*- coding: utf-8 -*-


def main():
    n = int(input())
    p = [int(input()) for _ in range(n)]
    print(sum(p) - max(p) // 2)


if __name__ == '__main__':
    main()
