# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = list(input().rstrip())

    for i in range(11):
        if n == n[::-1]:
            print("Yes")
            exit()

        n = ["0"] + n

    print("No")


if __name__ == "__main__":
    main()
