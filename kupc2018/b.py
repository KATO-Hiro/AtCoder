# -*- coding: utf-8 -*-


def main():
    from itertools import product

    h, w = map(int, input().split())
    c = [list(input()) for _ in range(h)]
    self_pos = c[h - 1].index('s')
    commands = [-1, 0, 1]
    roots = list(product(commands, repeat=h - 1))

    for root in roots:
        command_order = ''
        cur_pos = self_pos

        for i in range(h - 2, -1, -1):
            cur_pos += root[i]

            if 0 <= cur_pos < w and c[i][cur_pos] == '.':
                if root[i] == -1:
                    command_order += 'L'
                elif root[i] == 0:
                    command_order += 'S'
                else:
                    command_order += 'R'

        if len(command_order) == h - 1:
            print(command_order)
            exit()

    print('impossible')


if __name__ == '__main__':
    main()
