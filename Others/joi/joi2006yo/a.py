# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a_score, b_score = 0, 0

    for i in range(n):
        ai, bi = map(int, input().split())

        if ai > bi:
            a_score += ai + bi
        elif ai < bi:
            b_score += ai + bi
        else:
            a_score += ai
            b_score += bi

    print(a_score, b_score)


if __name__ == '__main__':
    main()
