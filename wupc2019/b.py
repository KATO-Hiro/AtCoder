# -*- coding: utf-8 -*-


def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    print(max(a))


if __name__ == '__main__':
    main()
