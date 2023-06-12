# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = bin(int(input()) - 1)[2:].zfill(10)
    n = n.replace("0", "4").replace("1", "7")
    print(n)


if __name__ == "__main__":
    main()
