# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = [input().rstrip() for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            sk = s[i] + s[j]

            if sk == sk[::-1]:
                print("Yes")
                exit()

    print("No")


if __name__ == "__main__":
    main()
