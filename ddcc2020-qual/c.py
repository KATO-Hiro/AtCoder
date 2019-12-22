# -*- coding: utf-8 -*-


def main():
    h, w, k = map(int, input().split())

    s = [list(input()) for _ in range(h)]
    has_strawberry = list()
    hi = list()
    wi = [[] for _ in range(w)]

    for index, si in enumerate(s):
        count = 0

        for sii in si:
            if sii == '#':
                count += 1

        if (index == 0 or index == h - 1) and (count == 0):
            hi.append(index)
        elif count > 0:
            hi.append(index)
            has_strawberry.append((index, count))

    for sb, count in has_strawberry:
        for index, sbi in enumerate(s[sb]):
            if sbi == "#":
                wi[sb].append(index)
    print(wi)

    print(has_strawberry)


if __name__ == '__main__':
    main()
