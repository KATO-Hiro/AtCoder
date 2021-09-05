# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    c = sorted(list(map(int, input().split())))
    ans = 0
    i, j, k = 0, 0, 0

    while i < n:
        while j < n:
            if a[i] < b[j]:
                break

            j += 1
        
        if j == n:
            break
        
        while j < n and k < n:
            if b[j] < c[k]:
                break

            k += 1

        if k == n:
            break
        
        ans += 1
        i, j, k = i + 1, j + 1, k + 1
        
    print(ans)


if __name__ == "__main__":
    main()
