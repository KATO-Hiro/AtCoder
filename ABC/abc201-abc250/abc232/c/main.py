# -*- coding: utf-8 -*-


def main():
    from itertools import permutations
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    ab = [[False] * n for _ in range(n)]
    
    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
    
        ab[ai][bi] = True
        ab[bi][ai] = True

    cd = [[0] * n for _ in range(n)]

    for _ in range(m):
        ci, di = map(int, input().split())
        ci -= 1
        di -= 1
    
        cd[ci][di] = True
        cd[di][ci] = True

    for p in permutations(range(n)):
        ok = True

        for i in range(n):
            for j in range(n):
                if ab[i][j] != cd[p[i]][p[j]]:
                    ok = False
                    break

        if ok:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
