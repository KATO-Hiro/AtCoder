# -*- coding: utf-8 -*-


def main():
    n, k = map(int, input().split())
    k -= 1
    t = input()
    print(t[:k] + t[k:].swapcase())


if __name__ == "__main__":
    main()
