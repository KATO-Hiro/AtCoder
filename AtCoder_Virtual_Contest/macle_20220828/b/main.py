# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    sc = [tuple(map(int, input().split())) for _ in range(m)]

    value_min = 10 ** (n - 1)
    value_max = 10 ** n

    if n == 1:
        value_min = 0

    for i in range(value_min, value_max):
        number = str(i)
        ok = True

        for si, ci in sc:
            si -= 1
            ci = str(ci)

            if number[si] != ci:
                ok = False
                break
        
        if ok:
            print(i)
            exit()
    
    print(-1)


if __name__ == "__main__":
    main()
