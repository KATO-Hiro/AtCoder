# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    print(''.join(sorted(list(s))))


if __name__ == "__main__":
    main()
