# -*- coding: utf-8 -*-


def main():
    from itertools import permutations

    s = list(input())

    print(len(set(list(permutations(s)))))


if __name__ == "__main__":
    main()
