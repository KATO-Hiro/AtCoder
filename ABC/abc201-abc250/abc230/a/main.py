# -*- coding: utf-8 -*-


def main():
    n = int(input())

    if n >= 42:
        n += 1

    ans = "AGC"
    print(ans + str(n).zfill(3))


if __name__ == "__main__":
    main()
