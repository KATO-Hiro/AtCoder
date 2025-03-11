# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n):
        if i + 2 >= n:
            break

        if a[i] == a[i + 1] == a[i + 2]:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
