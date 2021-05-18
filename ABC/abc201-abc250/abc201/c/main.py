# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    must = list()
    option = list()
    ans = 0

    for index, si in enumerate(s):
        if si == "o":
            must.append(index)
        elif si == "?":
            option.append(index)

    numbers = must + option
    must_set = set(must)

    for i in numbers:
        for j in numbers:
            for k in numbers:
                for l in numbers:
                    new_number = set([i, j, k, l])

                    if len(must_set) == len(must_set & new_number):
                        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
