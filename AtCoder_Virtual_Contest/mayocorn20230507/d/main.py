# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    path = list()

    # 右/下のみ移動すると考えても良い?
    for i in range(h):
        for j in range(w):
            if a[i][j] % 2 == 0:
                continue

            if j + 1 < w:
                a[i][j] -= 1 
                a[i][j + 1] += 1 

                path.append((i + 1, j + 1, i + 1, j + 2))
            elif i + 1 < h:
                a[i][j] -= 1 
                a[i + 1][j] += 1 

                path.append((i + 1, j + 1, i + 2, j + 1))
    
    print(len(path))

    for p in path:
        print(*p)


if __name__ == "__main__":
    main()
