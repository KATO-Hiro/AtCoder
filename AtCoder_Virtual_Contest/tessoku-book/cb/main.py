# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i == j:
                    continue
                if j == k:
                    continue
                if k == i:
                    continue

                if a[i] + a[j] + a[k] == 1000:
                    print("Yes")
                    exit()

    print("No")


if __name__ == "__main__":
    main()
