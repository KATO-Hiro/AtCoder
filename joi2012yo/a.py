# -*- coding: utf-8 -*-


def main():
    pasta_price = min([int(input()) for _ in range(3)])
    juice_price = min([int(input()) for _ in range(2)])
    print(pasta_price + juice_price - 50)


if __name__ == '__main__':
    main()
