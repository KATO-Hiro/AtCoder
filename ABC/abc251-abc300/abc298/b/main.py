# -*- coding: utf-8 -*-


from typing import List


# See:
# https://kazun-kyopro.hatenablog.com/entry/ABC/298/B
def rotate_90_degrees_to_right(array: List[List]):
    return [list(ai)[::-1] for ai in zip(*array)]


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
        
        c = rotate_90_degrees_to_right(c)

    print("No")
    

if __name__ == "__main__":
    main()
