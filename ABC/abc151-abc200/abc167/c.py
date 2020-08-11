# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n, m, x = map(int, input().split())
    c = list()
    a = list()

    for i in range(n):
        bi = list(map(int, input().split()))

        ci = bi[0]
        c.append(ci)

        ai = bi[1:]
        a.append(ai)

    ans = float('inf')

    # KeyInsight: bit演算を使った全探索
    # 全パターン(選ぶ/選ばないを1/0で表現)を列挙
    for i in range(1 << n):
        cost = 0
        tmp = [0 for _ in range(m)]

        for j in range(n):
            # あるビットが立っているかどうか(1かどうか)を判定
            if (i >> j & 1):
                cost += c[j]

                for index, aii in enumerate(a[j]):
                    tmp[index] += aii

        if min(tmp) >= x:
            ans = min(ans, cost)

    if ans == float('inf'):
        print(-1)
    else:
        print(ans)


if __name__ == '__main__':
    main()
