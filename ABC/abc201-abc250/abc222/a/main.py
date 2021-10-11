# -*- coding: utf-8 -*-


def main():
    n = input()
    m = len(n) 
    needed = 4 - m
    print(needed * '0' + ''.join(n))


if __name__ == "__main__":
    main()
