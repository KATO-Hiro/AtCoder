# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    q = list()
    ans = 0

    # See:
    # https://atcoder.jp/contests/abc240/submissions/29510382
    for ai in a:
        ans += 1

        if not q:
            q.append([ai, 1])
        elif ai != q[-1][0]:
            q.append([ai, 1])
        elif ai != q[-1][1] + 1:
            q[-1][1] += 1
        else:
            q.pop()
            ans -= ai
        
        print(ans)


if __name__ == "__main__":
    main()
