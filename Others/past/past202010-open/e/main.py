# -*- coding: utf-8 -*-


def main():
    from itertools import permutations

    n = int(input())
    s = input()

    for p in list(permutations(s, n)):
        si = "".join(map(str, p))

        if si != s and si != s[::-1]:
            print(si)
            exit()

    print("None")


if __name__ == "__main__":
    main()
