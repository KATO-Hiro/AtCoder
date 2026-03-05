# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    h, w, c1, c2 = input().rstrip().split()
    h, w = int(h), int(w)
    s = [list(input().rstrip()) for _ in range(h)]

    d = defaultdict(list)

    for i in range(h):
        for j in range(w):
            d[s[i][j]].append((i, j))

    for h1, w1 in d[c1]:
        for h2, w2 in d[c2]:
            if abs(h1 - h2) + abs(w1 - w2) == 1:
                print("Yes")
                exit()

    print("No")


if __name__ == "__main__":
    main()
