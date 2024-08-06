# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    h = list(map(int, input().split()))
    stack = []
    ans = []
    cur_s = 0

    # 水槽に水を注いで次の仕切りを超えるためには、階段状の長方形になっている必要がある
    # 上記の長方形をstackで管理
    for hi in h:
        wi = 1

        # stackが空でないかつ、stackの最後の要素 <= hiの場合に取り出す
        # 計算量: stackから取り出す回数 <= 追加する回数 (<= n)
        while stack and stack[-1][0] <= hi:
            prev_hj, prev_wj = stack.pop()
            wi += prev_wj
            cur_s -= prev_hj * prev_wj

        stack.append((hi, wi))

        cur_s += hi * wi
        ans.append(cur_s + 1)

    print(*ans)


if __name__ == "__main__":
    main()
