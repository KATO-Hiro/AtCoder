# -*- coding: utf-8 -*-


def main():
    n = int(input())
    p = list(map(int, input().split()))
    mod_p = sorted(p)
    count = 0

    for pi, mod_pi in zip(p, mod_p):
        if pi != mod_pi:
            count += 1

    if count <= 2:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
