# -*- coding: utf-8 -*-


def main():
    s = input()

    # See:
    # https://atcoder.jp/contests/abc039/submissions/5715840
    patterns = 'WBWBWWBWBWBW' * 10
    sounds = ['Do', 'Do', 'Re', 'Re', 'Mi', 'Fa', 'Fa', 'So', 'So', 'La', 'La', 'Si']

    for i in range(12):
        if s == patterns[i: i + 20]:
            ans = sounds[i]
            print(ans)
            exit()


if __name__ == '__main__':
    main()
