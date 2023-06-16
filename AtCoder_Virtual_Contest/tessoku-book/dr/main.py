# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    abc = sum(list(map(int, input().split())))

    if abc == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
