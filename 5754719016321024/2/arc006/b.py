# -*- coding: utf-8 -*-


def main():
    n, l = map(int, input().split())
    amida = [list(input()) for _ in range(l)]
    goal = list(input())
    print(amida)
    print(goal)

    i = 0
    j = 0

    while True:
        if (0 <= j + 2 <= 2 * n - 1):
            if amida[i][j + 1] == '-':
                j += 2
        # else:
        #     exit()

        # print(i)
        if 0 <= i + 1 < l:
            i += 1

            if i == l - 1:
                if goal[j] == 'o':
                    print(j + 1)
                    exit()
                else:
                    j += 2


if __name__ == '__main__':
    main()
