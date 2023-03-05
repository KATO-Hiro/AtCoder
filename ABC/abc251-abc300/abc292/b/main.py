# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    yellow = defaultdict(int)
    red = defaultdict(int)

    for _ in range(q):
        qi, x = map(int, input().split())

        if qi == 1:
            yellow[x] += 1
        elif qi == 2:
            red[x] += 2
        else:
            if yellow[x] >= 2 or red[x] >= 2:
                print("Yes")
            else:
                print("No")
    

if __name__ == "__main__":
    main()
