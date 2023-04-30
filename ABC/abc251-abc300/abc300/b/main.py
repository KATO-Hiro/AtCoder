# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    a = [list(input().rstrip()) for _ in range(h)]
    b = [list(input().rstrip()) for _ in range(h)]

    for s in range(h):
        for t in range(w):
            flag = True

            for i in range(h):
                for j in range(w):
                    if a[(i + s) % h][(j + t) % w] != b[i][j]:
                        flag = False
                
            if flag:
                print("Yes")
                exit()

    print("No")
    

if __name__ == "__main__":
    main()
