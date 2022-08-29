# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = [0] * (10 ** 6 + 1)
    a[2] = 1
    mod = 10007

    for i in range(3, n + 1):
        a[i] = a[i - 1] + a[i - 2] + a[i - 3]
        a[i] %= mod
    
    print(a[n - 1])



if __name__ == "__main__":
    main()
