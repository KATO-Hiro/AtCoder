# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    abc = sorted(list(map(int, input().split())), reverse=True)
    print("".join(map(str, abc)))


if __name__ == "__main__":
    main()
