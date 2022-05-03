# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = "".join(sorted(input().rstrip()))
    t = "".join(sorted(input().rstrip(), reverse=True))

    if s < t:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
