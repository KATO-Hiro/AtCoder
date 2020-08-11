# -*- coding: utf-8 -*-


def main():
    h, w = list(map(int, input().split()))
    removed = list()

    for i in range(h):
        ai = input()

        if ai.count('.') != w:
            removed.append(ai)

    ans = list()
    count = 0

    for j in range(len(removed[0])):
        is_black = False

        for i in range(len(removed)):
            if removed[i][j] == '#':
                is_black = True

        if is_black:
            for i in range(len(removed)):
                ans.append(removed[i][j])

            count += 1

    for m in range(len(ans) // count):
        result = ''

        for k in range(m, len(ans), len(ans) // count):
            result += ans[k]

        print(result)


if __name__ == '__main__':
    main()
