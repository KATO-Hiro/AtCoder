# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = [input().rstrip() for _ in range(n)]
    b = [input().rstrip() for _ in range(m)]

    for i in range(n - m + 1):
        for j in range(n - m + 1):
            count = 0

            for k in range(i, i + m):
                for l in range(j, j + m):
                    if a[k][l] == b[k - i][l - j]:
                        count += 1
            
            if count == m ** 2:
                print("Yes")
                exit()
    
    print("No")


if __name__ == "__main__":
    main()
