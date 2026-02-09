# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = [input().rstrip() for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i == j or j == k or k == i:
                    continue

                if s[i] + s[j] == s[k]:
                    print("Yes")
                    exit()

    print("No")


if __name__ == "__main__":
    main()
