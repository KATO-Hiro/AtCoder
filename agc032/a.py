# -*- coding: utf-8 -*-


def main():
    n = int(input())
    b = list(map(int, input().split()))
    ans = list()

    # KeyInsight
    # 数列aに数字を追加して数列bが作れるか?
    # ⇒数列bのk番目の値kを取り除くことができるか? と言い換える
    # https://www.youtube.com/watch?v=wOacBGq5OWU

    while b:
        index = -1
        candidate = -1

        # 一致するkが複数ある場合は，最も右側の値を選択
        for i, bi in enumerate(b, 1):
            if bi == i:
                index = i
                candidate = bi

        if index == -1:
            print(-1)
            exit()

        b.pop(index - 1)
        ans.append(candidate)

    # 最後の操作から行っているため，反転させる
    print('\n'.join(map(str, ans[::-1])))


if __name__ == '__main__':
    main()
