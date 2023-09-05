# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    abc = list(map(int, input().split()))
    abc2 = sorted(abc)

    if abc[1] == abc2[1]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
