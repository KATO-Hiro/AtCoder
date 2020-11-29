# -*- coding: utf-8 -*-


def main():
    from sys import setrecursionlimit

    setrecursionlimit(10 ** 7)

    n = int(input())

    def dfs(pattern, char_max):
        if len(pattern) == n:
            print(pattern)
            return

        for c in range(ord("a"), (char_max + 1) + 1):
            t = pattern
            t += chr(c)

            dfs(t, max(char_max, c))

    dfs("", ord("a") - 1)


if __name__ == "__main__":
    main()
