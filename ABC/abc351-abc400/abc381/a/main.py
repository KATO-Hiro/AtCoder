# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()

    if n % 2 == 1:
        t = "1" * (n // 2) + "/" + "2" * (n // 2)

        if s == t:
            print("Yes")
        else:
            print("No")
    else:
        print("No")


if __name__ == "__main__":
    main()
