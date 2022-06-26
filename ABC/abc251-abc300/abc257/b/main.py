# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    b = [0] * n

    for index, ai in enumerate(a):
        b[ai - 1] = 1

    for i, li in enumerate(l):
        count = 0
        
        for j in range(n - 1):
            if b[j] == 1:
                count += 1

            if count == li:
                if j + 1 > n - 1:
                    continue
                if b[j + 1] == 0:
                    b[j + 1] = 1
                    b[j] = 0

                break
        
    ans = list()
    
    for i, bi in enumerate(b, 1):
        if bi == 1:
            ans.append(i)

    print(*ans)


if __name__ == "__main__":
    main()
