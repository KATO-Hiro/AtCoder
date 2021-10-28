# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = input()

    for si, ti in zip(s, s[1:]):
        if ti == "J":
            print(si)


if __name__ == "__main__":
    main()
