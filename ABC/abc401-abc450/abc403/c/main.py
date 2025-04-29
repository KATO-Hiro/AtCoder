# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, m, q = map(int, input().split())
    view = defaultdict(set)
    view_all = set()

    for _ in range(q):
        query = list(map(int, input().split()))

        if query[0] == 1:
            x, y = query[1:]
            view[x].add(y)
        elif query[0] == 2:
            x = query[1]
            view_all.add(x)
        else:
            x, y = query[1:]

            if x in view_all or y in view[x]:
                print("Yes")
            else:
                print("No")


if __name__ == "__main__":
    main()
