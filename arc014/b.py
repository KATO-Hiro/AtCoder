# -*- coding: utf-8 -*-


def main():
    n = int(input())
    ws = [input() for _ in range(n)]
    used_words = set()
    used_words.add(ws[0])

    for i in range(1, n):
        if (ws[i][0] != ws[i - 1][-1]) or ws[i] in used_words:
            if i % 2 == 0:
                print('LOSE')
                exit()
            else:
                print('WIN')
                exit()

        used_words.add(ws[i])

    print('DRAW')


if __name__ == '__main__':
    main()
