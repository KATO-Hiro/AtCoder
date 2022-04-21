# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = [input().rstrip().count('1') == 4 for _ in range(4)]
    print(sum(s))


if __name__ == "__main__":
    main()
