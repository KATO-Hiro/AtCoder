# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = list(input().rstrip())
    q = int(input())
    id = -1
    t, x, c = list(), list(), list()

    # クエリ先読み
    for i in range(q):
        qi = input().rstrip().split()
        t.append(qi[0])
        x.append(int(qi[1]) - 1)
        c.append(qi[2])

        if qi[0] != "1":
            id = i

    # print(t, x, c)
    # print(id)

    for i, (ti, xi, ci) in enumerate(zip(t, x, c)):
        # print(ti, xi, ci)

        if i == id and ti != "1":
            if ti == "2":
                for i in range(n):
                    s[i] = s[i].lower()
            elif ti == "3":
                for i in range(n):
                    s[i] = s[i].upper()
        elif i != id and ti == "1":
            s[xi] = ci

    print("".join(s))


if __name__ == "__main__":
    main()
