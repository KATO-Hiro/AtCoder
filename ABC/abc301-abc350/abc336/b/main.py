# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = bin(int(input()))[2:][::-1]
    m = len(n)
    i = 0
    count = 0

    while i < m:
        if n[i] == "0":
            count += 1
        else:
            break

        i += 1

    print(count)


if __name__ == "__main__":
    main()
