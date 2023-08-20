# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()[::-1]
    n = len(list(s))

    for i in range(2, n, 2):
        mid = (n - i) // 2
        # print(s[i : i + mid], s[i + mid :])

        if s[i : i + mid] == s[i + mid :]:
            print(n - i)
            exit()


if __name__ == "__main__":
    main()
