# -*- coding: utf-8 -*-


def main():
    a = [input().split() for _ in range(3)]
    ans = [[0] * 3 for _ in range(3)]
    n = int(input())
    b = [input() for _ in range(n)]

    for bi in b:
        for y in range(3):
            for x in range(3):
                if bi == a[y][x]:
                    ans[y][x] = 1

    if ans[0][0] == ans[0][1] == ans[0][2] == 1:
        print('Yes')
    elif ans[1][0] == ans[1][1] == ans[1][2] == 1:
        print('Yes')
    elif ans[2][0] == ans[2][1] == ans[2][2] == 1:
        print('Yes')
    elif ans[0][0] == ans[1][0] == ans[2][0] == 1:
        print('Yes')
    elif ans[0][1] == ans[1][1] == ans[2][1] == 1:
        print('Yes')
    elif ans[0][2] == ans[1][2] == ans[2][2] == 1:
        print('Yes')
    elif ans[0][0] == ans[1][1] == ans[2][2] == 1:
        print('Yes')
    elif ans[0][2] == ans[1][1] == ans[2][0] == 1:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
