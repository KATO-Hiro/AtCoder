# -*- coding: utf-8 -*-


def main():
    alpha = [0 for _ in range(3)]
    s = input()

    # KeyInsight
    # abcabcabc...の形にできれば回文にならない
    for si in s:
        if si == 'a':
            alpha[0] += 1
        elif si == 'b':
            alpha[1] += 1
        else:
            alpha[2] += 1

    # a, b, cの出現回数の差が1以下なら回文にならない
    if max(alpha) - min(alpha) <= 1:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
