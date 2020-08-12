# -*- coding: utf-8 -*-


def main():
    from itertools import product

    a = map(int, input().split())
    b = map(int, input().split())
    c = int(input())
    ans = set()

    for ai, bi in list(product(a, b)):
        if ai == c:
            ans.add(bi)
        if bi == c:
            ans.add(ai)

    print(len(ans))

    for ans_i in sorted(ans):
        print(ans_i)


if __name__ == '__main__':
    main()
