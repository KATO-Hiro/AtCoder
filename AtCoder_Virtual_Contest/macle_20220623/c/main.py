# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, h = map(int, input().split())
    ab = list()
    inf = float('inf')

    for i in range(n):
        ai, bi = map(int, input().split())
        ab.append((ai, i, inf))
        ab.append((bi, i, 1))
    
    ans = 0
    used_bi = [False] * n

    for ci, index, count in sorted(ab, reverse=True):
        if count == inf:
            p, q = divmod(h, ci)
            ans += p

            if q > 0:
                ans += 1
            
            print(ans)
            exit()
        else:
            h -= ci
            ans += 1
            used_bi[index] = True

        if h <= 0:
            print(ans)
            exit()


if __name__ == "__main__":
    main()
