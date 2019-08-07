# -*- coding: utf-8 -*-


def main():
    from itertools import permutations

    n, m = map(int, input().split())
    graph = [[0 for __ in range(n)] for _ in range(n)]
    ans = 0

    for i in range(m):
        ai, bi = map(lambda x: int(x) - 1, input().split())
        graph[ai][bi] = 1
        graph[bi][ai] = 1

    for j in list(permutations(range(n))):
        count = 0

        if j[0] == 0:
            for k in range(n - 1):
                _from = j[k]
                _to = j[k + 1]

                if graph[_from][_to] == 1:
                    count += 1

            if count == n - 1:
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()
