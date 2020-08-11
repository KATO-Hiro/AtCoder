# -*- coding: utf-8 -*-


def main():
    n = int(input())
    rest = dict()

    for i in range(n):
        si, pi = input().split()

        if si not in rest.keys():
            rest[si] = [(i + 1, int(pi))]
        else:
            rest[si].append((i + 1, int(pi)))

    for key, values in sorted(rest.items(), key=lambda x: x[0]):
        for no, values in sorted(values, key=lambda y: y[1], reverse=True):
            print(no)


if __name__ == '__main__':
    main()
