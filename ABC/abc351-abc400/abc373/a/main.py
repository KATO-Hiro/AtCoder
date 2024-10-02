# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline
    count = 0

    for i in range(1, 13):
        si = input().rstrip()

        if len(si) == i:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
