# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    r, c = map(int, input().split())
    b = [list(input().rstrip()) for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if b[i][j] == "." or b[i][j] == "#":
                continue
        
            d = int(b[i][j])

            for ni in range(r):
                for nj in range(c):
                    if abs(i - ni) + abs(j - nj) > d:
                        continue

                    if 0 <= ni < r and 0 <= nj < c:
                        if b[ni][nj] == "#":
                            b[ni][nj] = "."
            
            b[i][j] = "."
        
    for bi in b:
        print(*bi, sep="")


if __name__ == "__main__":
    main()
