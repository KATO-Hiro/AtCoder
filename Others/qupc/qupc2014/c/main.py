# -*- coding: utf-8 -*-


def main():
    from string import ascii_uppercase

    n, m, q_large = map(int, input().split())
    s = [list(input()) for _ in range(n)]
    q = [input() for _ in range(q_large)]
    pos = [None for _ in range(26)]

    for i in range(n):
        for j in range(m):
            sij = s[i][j]
            if sij != "*":
                index = ascii_uppercase.index(sij)
                pos[index] = (i + 1, j + 1)

    for qi in q:
        index = ascii_uppercase.index(qi)
        p = pos[index]

        if p is None:
            print("NA")
        else:
            print(p[0], p[1])


if __name__ == "__main__":
    main()
