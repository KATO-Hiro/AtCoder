# -*- coding: utf-8 -*-


def main():
    s = input()
    k = int(input())

    prev = s[0]
    count = 1
    pair = list()

    # 文字と連続する回数を数える
    for cur in s[1:]:
        if cur == prev:
            count += 1
        else:
            pair.append((prev, count))
            prev = cur
            count = 1

    if count >= 1:
        pair.append((prev, count))

    # Sの文字が1種類かどうか
    if len(pair) == 1:
        # WAの原因：kが偶奇の場合で場合分けしていたが不要だった
        print(len(s) * k // 2)
    else:
        first = pair[0]
        last = pair[-1]
        ans = 0

        # 両端が同じ文字の種類
        if first[0] == last[0]:
            for a, count in pair[1:-1]:
                ans += count // 2

            print(ans * k + first[1] // 2 + last[1] // 2 + (first[1] + last[1]) // 2 * (k - 1))
        else:
            for a, count in pair:
                ans += count // 2

            print(ans * k)


if __name__ == '__main__':
    main()
