# -*- coding: utf-8 -*-


def main():
    from collections import deque

    s = deque(input())
    ans = 0

    # KeyInsight
    # 回文の判定：最初と最後の文字が一致しているかどうか
    # データ構造：文字の取り出しと削除を高速に行う
    while s:
        # 先頭の文字を取り出す
        first = s.popleft()

        if len(s) >= 1:
            # 残りが1文字以上なら，末尾の文字を取り出す
            last = s.pop()
        else:
            # 残り0文字なら終了
            print(ans)
            exit()

        # 先頭と末尾が一致なら，そのまま
        if first == last:
            pass
        # 先頭x，末尾がx以外→末尾にxを追加
        # 操作が1回増える
        elif first == 'x' and last != 'x':
            s.appendleft(first)
            s.append(last)
            s.append('x')
            ans += 1
        # 先頭x以外，末尾がx→先頭にxを追加
        # 操作が1回増える
        elif first != 'x' and last == 'x':
            s.appendleft(first)
            s.appendleft('x')
            s.append(last)
            ans += 1
        # それ以外 -1, 終了
        else:
            print(-1)
            exit()

    print(ans)


if __name__ == '__main__':
    main()
