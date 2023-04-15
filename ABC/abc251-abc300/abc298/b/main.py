# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    b = [list(map(int, input().split())) for _ in range(n)]
    c = a.copy()
    ans = "Yes"

    for _ in range(4):
        tmp = True

        for i in range(n):
            for j in range(n):
                if c[i][j] == 0:
                    continue

                if b[i][j] == 0:
                    tmp = False
                    break
        
        if tmp:
            print(ans)
            exit()
        
        d = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                d[i][j] = c[n - 1 - j][i]
        
        c = d

    print("No")
    

if __name__ == "__main__":
    main()
