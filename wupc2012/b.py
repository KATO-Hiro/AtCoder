# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = [input() for _ in range(n)]
    ans = list()

    # See:
    # https://atcoder.jp/contests/wupc2012/submissions/4888916
    # 全探索
    # sを昇順にして，最初の要素2つ取るだけではWAが2個あった
    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            ans.append(s[i] + s[j])

    print(min(ans))


if __name__ == '__main__':
    main()
