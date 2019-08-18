# -*- coding: utf-8 -*-


def main():
    s = input()
    n = len(s)
    pre = ''
    ans = 0
    i = 0

    # See:
    # https://atcoder.jp/contests/agc037/submissions/6955216
    while i < n:
        cur = s[i]

        if pre == cur:
            if i + 1 < n:
                pre = cur + s[i + 1]
                # 1文字増やすことに伴い，参照するインデックスも修正
                i += 1
            # 末尾の処理
            else:
                break
        else:
            pre = cur

        ans += 1
        i += 1

    print(ans)


if __name__ == '__main__':
    main()
