# -*- coding: utf-8 -*-


def main():
    n, x = map(int, input().split())
    max_b = 0
    liked_point = 0

    for i in range(n):
        ai, bi = map(int, input().split())
        liked_point += ai * bi
        max_b = max(max_b, bi)

    print(liked_point + x * max_b)


if __name__ == '__main__':
    main()
