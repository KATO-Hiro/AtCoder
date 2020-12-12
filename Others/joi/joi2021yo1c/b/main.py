# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = input()
    count = 0

    for index, si in enumerate(s):
        if index % 2 == 0:
            if si != "I":
                count += 1
        else:
            if si != "O":
                count += 1

    print(count)


if __name__ == "__main__":
    main()
