# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    red = list()
    blue = list()

    for i in range(n):
        xi, ci = input().split()

        if ci == 'R':
            red.append(int(xi))
        else:
            blue.append(int(xi))

    print('\n'.join(map(str, sorted(red))))
    print('\n'.join(map(str, sorted(blue))))


if __name__ == '__main__':
    main()
