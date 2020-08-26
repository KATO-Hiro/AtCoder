# -*- coding: utf-8 -*-


def main():
    s = input()
    n = len(s)
    k = int(input())
    candidates = set()

    for j in range(min(n, k)):
        for i in range(n - j):
            candidates.add(s[i:i + j + 1])

    print(sorted(candidates)[k - 1])


if __name__ == '__main__':
    main()
