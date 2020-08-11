# -*- coding: utf-8 -*-


def main():
    total = int(input())
    nine_books_price = sum([int(input()) for _ in range(9)])
    print(total - nine_books_price)


if __name__ == '__main__':
    main()
