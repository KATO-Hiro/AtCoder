# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a = [list(map(int, input().split())) for _ in range(9)]
    ac_count = 0
    wa_count = 0

    for i in range(9):
        for j in range(9):
            k = (i + 1) * (j + 1)

            if a[i][j] == k:
                ac_count += 1
            else:
                a[i][j] = k
                wa_count += 1
    
    for ai in a:
        print(*ai)

    print(ac_count)
    print(wa_count)


if __name__ == "__main__":
    main()
