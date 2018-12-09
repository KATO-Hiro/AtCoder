# -*- coding: utf-8 -*-


def main():
    s = input()
    n_count = s.count('N')
    s_count = s.count('S')
    e_count = s.count('E')
    w_count = s.count('W')

    if n_count > 0 and s_count == 0:
        print('No')
    elif s_count > 0 and n_count == 0:
        print('No')
    elif e_count > 0 and w_count == 0:
        print('No')
    elif w_count > 0 and e_count == 0:
        print('No')
    else:
        print('Yes')


if __name__ == '__main__':
    main()
