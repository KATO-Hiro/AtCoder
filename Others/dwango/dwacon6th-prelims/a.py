# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = list()
    t = list()

    for i in range(n):
        si, ti = map(str, input().split())
        s.append(si)
        t.append(int(ti))

    x = input()
    index = s.index(x)
    print(sum(t[index + 1:]))


if __name__ == '__main__':
    main()
