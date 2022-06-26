# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))

    for i in range(q):
        if a[l[i] - 1] == n:
            continue
        elif l[i] == k:
            a[l[i] - 1] += 1
        elif a[l[i] - 1] + 1 < a[l[i]]:
            a[l[i] - 1] += 1
        
    print(*a)


if __name__ == "__main__":
    main()
