# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, t = map(int, input().split())
    remain = n
    last = 0

    for i in range(m):
        ai, bi = map(int, input().split())
        remain -= (ai - last)

        if remain <= 0:
            print("No")
            exit()
        
        remain += (bi - ai)
        remain = min(remain, n)
        last = bi
        
    remain -= (t - last)

    if remain <= 0:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
