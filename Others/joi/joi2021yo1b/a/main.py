# -*- coding: utf-8 -*-


def main():
    a, b, c = map(int, input().split())

    if a <= c < b:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    main()
