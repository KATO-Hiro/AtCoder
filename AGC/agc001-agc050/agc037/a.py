# -*- coding: utf-8 -*-


def main():
    s = input()
    prev, cur = '', ''
    ans = 0

    for si in s:
        cur += si  # KeyInsight: curに1文字加える

        # prevとcurが異なる
        if cur != prev:
            ans += 1

            # prevとcurを更新
            prev = cur
            cur = ''

    print(ans)


if __name__ == '__main__':
    main()
