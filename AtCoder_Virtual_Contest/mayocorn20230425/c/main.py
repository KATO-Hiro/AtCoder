# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * n
    c = sorted(a)

    for i in range(k):
        j = 0
        tmp = list()

        while (i + j * k) < n:
            tmp.append(a[i + j * k])
            j += 1
        
        tmp = sorted(tmp)
        j = 0

        while (i + j * k) < n:
            b[i + j * k] = tmp[j]
            j += 1
    
    if b == c:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
