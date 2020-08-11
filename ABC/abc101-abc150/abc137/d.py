# -*- coding: utf-8 -*-


def main():
    # ヒープキューをインポート
    from heapq import heappush, heappop

    n, m = map(int, input().split())
    jobs = [[] for _ in range(m)]  # 締め切り別に，報酬を管理

    # See:
    # https://www.youtube.com/watch?v=1Z6ofKN03_Y
    for i in range(n):
        ai, bi = map(int, input().split())

        # 報酬が振り込まれる日がM日よりも後になる場合は除外
        if ai > m:
            continue

        # i件目のアルバイトを遅くてもいつまでに始める必要があるかを計算
        # heappopは最小値を返す．biを-1倍することで，最大値が取り出せる
        deadline = m - ai
        jobs[deadline].append(-bi)

    ans = 0
    reward = []

    # M-1日に始める必要があるアルバイトのうち，最も報酬の高いものを選択
    # 以降，今日始める必要があるアルバイトまで，順番に調べる
    # ある時点で得られる報酬の大小に着目
    for i in range(m - 1, -1, -1):
        for job in jobs[i]:
            # ヒープキューに，報酬の候補を追加
            heappush(reward, job)

        # 条件を満たすもののうち，最大の報酬を選択
        if reward:
            ans += heappop(reward)

    # ヒープキューに追加するときに，-1倍した分を元に戻す
    print(-ans)


if __name__ == '__main__':
    main()
