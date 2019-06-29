# -*- coding: utf-8 -*-


def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    mod_ab = sorted(ab, key=lambda x: (x[1], x[0]))
    time = 0

    for ai, bi in mod_ab:
        time += ai

        if time > bi:
            print('No')
            exit()

    print('Yes')


if __name__ == '__main__':
    main()
