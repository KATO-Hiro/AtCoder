# -*- coding: utf-8 -*-


def main():
    cs = list()

    for i in range(4):
        cs.append(list(map(str, input().split())))

    for c in reversed(cs):
        print(' '.join(c[::-1]))


if __name__ == '__main__':
    main()
