# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    a = [list(input().rstrip()) for _ in range(h)]
    b = [list(input().rstrip()) for _ in range(h)]

    for i in range(h):
        c = list()

        for ii in range(h):
            ni = (i + ii) % h
            c.append(a[ni])

        for j in range(w):
            d = list()

            for jj in range(w):
                nj = (j + jj) % w

                for k in range(h):
                    ck = c[k]
                    d.append(ck[nj:] + ck[:nj])
            
            flag = True

            for y in range(h):
                for x in range(w):
                    if d[y][x] != b[y][x]:
                        flag = False
                        break

            if flag:
                print("Yes")
                exit()

    print("No")
    

if __name__ == "__main__":
    main()
