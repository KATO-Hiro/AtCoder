# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w, c = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    inf = 10 ** 18
    ans = inf

    for _ in range(2):
        cost = [[inf for _ in range(w)] for _ in range(h)]

        for i in range(h):
            for j in range(w):
                if i > 0:
                    cost[i][j] = min(cost[i][j], cost[i - 1][j])
                if j > 0:
                    cost[i][j] = min(cost[i][j], cost[i][j - 1])
                
                ans = min(ans, a[i][j] + c * (i + j) + cost[i][j])

                cost[i][j] = min(cost[i][j], a[i][j] - c * (i + j))
        
        a = a[::-1]
    
    print(ans)


if __name__ == "__main__":
    main()
