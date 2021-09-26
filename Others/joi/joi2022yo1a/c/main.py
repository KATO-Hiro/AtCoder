# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = set(list(input()))

    if len(s) >= 3:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
