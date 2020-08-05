# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    ans = 0

    if a[0] > 0:
        print(-1)
        exit()

    # KeyInsight:
    # ◯: 2マスの値を比べる。
    #    右側 - 左側 = 1のときは、答えに1加算。
    #    同じ値のときは、その値を答えに加算。
    # ◯: a0以外のときと、2マスの差が2以上のときは、条件を満たさない。
    # △: 上記の考察を実装したが、10ケースWA。
    # △: 条件を満たさない場合を先に持ってくると、その後の条件がシンプルに。

    # See:
    # https://atcoder.jp/contests/agc024/submissions/15705631
    for pre, cur in zip(a, a[1:]):
        if pre + 1 < cur:
            print(-1)
            exit()

        if pre + 1 == cur:
            ans += 1
        else:
            ans += cur

    print(ans)


if __name__ == '__main__':
    main()
