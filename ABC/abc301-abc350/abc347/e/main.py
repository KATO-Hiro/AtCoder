# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    x = list(map(int, input().split()))
    s = set()
    size, acc = 0, 0
    ans = [0] * n

    # 動的に累積和を更新
    for xi in x:
        xi -= 1

        if xi in s:
            s.discard(xi)
            size -= 1
            ans[xi] += acc
        else:
            s.add(xi)
            size += 1
            ans[xi] -= acc

        acc += size

    # クエリの最後まで、要素が削除されない場合への対応
    for si in s:
        ans[si] += acc

    print(*ans)


if __name__ == "__main__":
    main()
