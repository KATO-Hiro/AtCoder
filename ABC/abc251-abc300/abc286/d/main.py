# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    a1, b1 = ab[0]
    ans = set([a1 * bi for bi in range(b1 + 1) if a1 * bi <= x])

    for i in range(1, n):
        ai, bi = ab[i]
        c = [ai * bi for bi in range(bi + 1) if ai * bi <= x]
        d = ans
        tmp = set()

        for di in d:
            for ci in c:
                ei = di + ci

                if ei <= x:
                    tmp.add(ei)

        ans |= tmp

    if x in ans:
        print("Yes")
    else:
        print("No")
    

if __name__ == "__main__":
    main()
