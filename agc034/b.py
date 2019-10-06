# -*- coding: utf-8 -*-


def main():
    s = input()
    # 判定をシンプルにするため，'BC'を'D'と置き換える
    # ループを扱いやすくするため，リストを反転させる
    mod_s = list(s.replace('BC', 'D'))[::-1]
    d_count = 0
    ans = 0

    # 文字列にBCが存在する必要がある
    # 操作をよく見ると，BCの左側にあるAを右側に移動させていることと同じ
    # BCが出現してから，
    #   1. Aが現れたときはBCを飛び越えた回数を答えに加算
    #   2. BCが現れたら，BCを管理する変数のカウントを1増やす
    #   3. BかCが単独で現れたら，BCを管理する変数のカウントをリセット
    for si in mod_s:
        if si == 'D':
            d_count += 1
        elif si == 'A':
            ans += d_count
        else:
            d_count = 0

    print(ans)


if __name__ == '__main__':
    main()
