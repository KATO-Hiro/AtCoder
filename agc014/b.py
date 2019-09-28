# -*- coding: utf-8 -*-


def main():
    n, m = map(int, input().split())
    c = [0 for _ in range(n)]

    # KeyInsight
    # https://www.youtube.com/watch?v=UHfTqvaD0pk：
    # とっかかりとして，根付き木を考える（最終的には，木の形状は関係ない）
    # 始点x，終点yとして，根をrとする．
    # x -> yを x -> r, y -> rの形に分解
    # 関心があるのは偶奇のみ，同じ操作が偶数回あるときは操作しないことと同じ
    # x, yの登場回数がすべて偶数ならYES，奇数が1つでもあればNO
    for i in range(m):
        ai, bi = map(int, input().split())
        # 0-index
        ai -= 1
        bi -= 1
        c[ai] += 1
        c[bi] += 1

    for ci in c:
        if ci % 2 == 1:
            print('NO')
            exit()

    print('YES')


if __name__ == '__main__':
    main()
