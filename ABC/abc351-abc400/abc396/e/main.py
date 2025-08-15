# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        ai, bi, zi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append((bi, zi))
        graph[bi].append((ai, zi))

    pending = -1

    def bfs(start):
        q = deque([start])
        colors[start] = 0
        zero_or_one[0].append(start)

        while q:
            cur = q.popleft()
            color = colors[cur]

            for to, zi in graph[cur]:
                expected_color = color ^ (zi >> digit & 1)

                if colors[to] != pending:
                    if colors[to] != expected_color:
                        return False
                else:
                    colors[to] = expected_color
                    zero_or_one[expected_color].append(to)
                    q.append(to)

        return True

    ans = [0] * n

    # XORは、桁ごとで独立に扱える
    for digit in range(30):
        colors = [pending] * n

        # 0 / 1 の割り当てを2色で塗り分ける問題と言い換え
        for i in range(n):
            if colors[i] != pending:
                continue

            # 連結成分単位で管理
            zero_or_one = [[], []]

            if not bfs(i):
                print(-1)
                exit()

            # 各bitに対して、1の割り当てる個数を減らす
            zero_count, one_count = len(zero_or_one[0]), len(zero_or_one[1])

            if zero_count < one_count:
                zero_or_one[0], zero_or_one[1] = zero_or_one[1], zero_or_one[0]

            for one_id in zero_or_one[1]:
                ans[one_id] |= 1 << digit

    print(*ans)


if __name__ == "__main__":
    main()
