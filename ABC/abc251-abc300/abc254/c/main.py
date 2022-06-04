# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    c = sorted(a)
    b = [0] * n
    t = list()

    for i in range(k):
        s = sorted(a[i::k])
        t.append(s)
    
    for i, ti in enumerate(t):
        for j, tii in enumerate(ti):
            b[i + j * k] = tii
    
    if b == c:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
