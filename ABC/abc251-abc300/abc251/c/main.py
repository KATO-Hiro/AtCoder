# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline
    n = int(input())
    s = set()
    candidates = list()

    # 処理を分割
    # オリジナルか判定
    for i in range(n):
        si, ti = map(str, input().split())

        if si in s:
            continue 
        else:
            candidates.append((int(ti), i + 1))
            s.add(si)

    highest = 0 
    id = 1

    # スコアの最大値を求める
    for score, index in candidates:
        if score > highest:
            highest = score
            id = index

    print(id)


if __name__ == "__main__":
    main()
