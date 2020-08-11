# -*- coding: utf-8 -*-


def main():
    s = input()
    upper_count = 0
    word = ''
    words = list()

    for si in s:
        # 探索する文字が大文字か判定
        if si.isupper():
            upper_count += 1

        word += si

        # 問題文通り、大文字2個で区切る
        if upper_count == 2:
            words.append(word)
            upper_count = 0
            word = ''

    # 組み込み関数で、大文字と小文字を区別せずに比較する
    # https://docs.python.org/ja/3/howto/sorting.html
    print(''.join(sorted(words, key=str.lower)))


if __name__ == '__main__':
    main()
