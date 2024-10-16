# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    count = 0

    for i in range(n):
        if i + 2 >= n:
            break

        if s[i] == s[i + 2] == "#" and s[i + 1] == ".":
            count += 1

    print(count)


if __name__ == "__main__":
    main()
