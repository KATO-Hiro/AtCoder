# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    w, h = map(int, input().split())
    a, b = map(int, input().split())
    c = [list(map(int, input().split())) for _ in range(h)]
    # print(c)
    people_count = 0
    cost = 0
    inf = 10**18
    ans = inf

    def f(candidate, count):
        if count == 0:
            return min(ans, candidate)
        else:
            return ans

    # 一つ目の候補地を全探索 + 差分を考える
    for i in range(b):
        for j in range(a):
            if c[i][j] == -1:
                people_count += 1
            else:
                cost += c[i][j]

    ans = f(cost, people_count)
    cost2 = cost
    people_count2 = people_count

    for k in range(a, w):
        for l in range(b):
            if c[l][k] == -1:
                people_count2 += 1
            else:
                cost2 += c[l][k]
                cost2 -= c[l][k - a]

                if c[l][k - a] == -1:
                    people_count2 -= 1

        ans = f(cost2, people_count2)

    for y in range(b, h):
        for x in range(a):
            if c[y][x] == -1:
                people_count += 1
            else:
                cost += c[y][x]
                cost -= c[y - b][x]

                if c[y - b][x] == -1:
                    people_count -= 1

        ans = f(cost, people_count)
        print(cost, people_count)

        # cost3 = cost

        # for k in range(a, w):
        #     for l in range(y - b + 1, y + 1):
        #         if c[l][k] == -1:
        #             people_count += 1
        #         else:
        #             cost3 += c[l][k]
        #             cost3 -= c[l][k - a]

        #             if c[l][k - a] == -1:
        #                 people_count -= 1

        #     ans = f(cost3)

    print(ans)


if __name__ == "__main__":
    main()
