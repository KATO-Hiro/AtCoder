# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    b = [list(map(int, input().split())) for _ in range(h)]
    ans = 0

    for i in range(h):
        for j in range(w):
            if i + 1 >= h or j + 1 >= w:
                continue

            diff = abs(a[i][j] - b[i][j])

            if a[i][j] > b[i][j]:
                a[i][j] -= diff
                a[i + 1][j] -= diff
                a[i][j + 1] -= diff
                a[i + 1][j + 1] -= diff
            elif a[i][j] < b[i][j]:
                a[i][j] += diff
                a[i + 1][j] += diff
                a[i][j + 1] += diff
                a[i + 1][j + 1] += diff

            ans += diff
    
    for i in range(h):
        for j in range(w):
            if a[i][j] != b[i][j]:
                print("No")
                exit()
    
    print("Yes")
    print(ans)

if __name__ == "__main__":
    main()
