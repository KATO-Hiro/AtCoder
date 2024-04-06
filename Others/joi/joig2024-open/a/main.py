# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()

    for i in range(n):
        if i + 2 >= n:
            break

        if s[i] == s[i + 1] == s[i + 2] == "o":
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
