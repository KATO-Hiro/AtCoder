# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    t = input().rstrip()
    s += ".."
    t += ".."

    # 操作回数の最小化問題を最短経路問題に言い換え
    dist = dict()
    dist[s] = 0
    # マスの並びそのものを状態として持つ
    # 状態数: 15! / (7! * 7! * 1!) ≒ 5 * 10 ** 4
    q = deque([s])

    while q:
        cur_s = q.popleft()

        # ..の左側の位置を探す
        empty_left = cur_s.find(".")

        # 遷移: グラフを持つ代わりに、
        # 両方石が置かれているマスをすべて列挙
        for i in range(n + 1):
            if cur_s[i] == "." or cur_s[i + 1] == ".":
                continue

            next_s = list(cur_s)
            # swap
            next_s[i], next_s[empty_left] = next_s[empty_left], next_s[i]
            next_s[i + 1], next_s[empty_left + 1] = (
                next_s[empty_left + 1],
                next_s[i + 1],
            )

            if "".join(next_s) in dist.keys():
                continue

            dist["".join(next_s)] = dist[cur_s] + 1
            q.append("".join(next_s))

    if t in dist.keys():
        print(dist[t])
    else:
        print(-1)


if __name__ == "__main__":
    main()
