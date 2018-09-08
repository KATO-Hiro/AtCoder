# -*- coding: utf-8 -*-


def main():
    n = int(input())
    word = list()
    pre_word = input()
    word.append(pre_word)

    for i in range(n - 1):
        w = input()

        if w not in word:
            word.append(w)

            if pre_word[-1] != w[0]:
                print('No')
                exit()
        else:
            print('No')
            exit()

        pre_word = w

    print('Yes')


if __name__ == '__main__':
    main()
