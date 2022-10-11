# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    q = list()  # number, count
    ans = 0

    for ai in a:
        ans += 1

        # 場合分け: より制約の厳しい条件から判定
        if not q:
            q.append([ai, 1])
        elif ai != q[-1][0]:
            q.append([ai, 1])
        elif ai != q[-1][1] + 1:
            q[-1][1] += 1
        else:
            q.pop()
            ans -=ai

        print(ans)


if __name__ == "__main__":
    main()
