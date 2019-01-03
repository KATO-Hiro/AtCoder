# -*- coding: utf-8 -*-


def main():
    n = int(input())
    words = list()
    word = input()
    words.append(word)
    prev = word[-1]

    for i in range(n - 1):
        cur = input()

        if cur in words:
            print('No')
            exit()

        if prev != cur[0]:
            print('No')
            exit()

        words.append(cur)
        prev = cur[-1]

    print('Yes')


if __name__ == '__main__':
    main()
