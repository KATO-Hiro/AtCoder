# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    i, j = input().rstrip().split("-")
    i, j = int(i), int(j)

    if j == 8:
        i += 1
        j = 1
    else:
        j += 1

    print(f"{i}-{j}")


if __name__ == "__main__":
    main()
