# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    product_a = 1
    product_b = 1

    for ai in a:
        product_a *= ai

    for bi in b:
        product_b *= bi

    if product_a == product_b:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
