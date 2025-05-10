# -*- coding: utf-8 -*-


def main():
    import sys
    from string import ascii_lowercase

    input = sys.stdin.readline

    s = input().rstrip()

    for alpha in ascii_lowercase:
        if alpha not in s:
            print(alpha)
            exit()


if __name__ == "__main__":
    main()
