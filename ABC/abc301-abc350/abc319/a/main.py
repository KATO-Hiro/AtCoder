# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    ps = [
        ["tourist", 3858],
        ["ksun48", 3679],
        ["Benq", 3658],
        ["Um_nik", 3648],
        ["apiad", 3638],
        ["Stonefeang", 3630],
        ["ecnerwala", 3613],
        ["mnbvmar", 3555],
        ["newbiedmy", 3516],
        ["semiexp", 3481],
    ]

    s = input().rstrip()
    # print(s)

    for name, rate in ps:
        if s == name:
            print(rate)
            exit()


if __name__ == "__main__":
    main()
