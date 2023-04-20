# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    sa = list(input().rstrip())
    sb = list(input().rstrip())
    sc = list(input().rstrip())
    da = deque(sa)
    db = deque(sb)
    dc = deque(sc)
    player = "a"

    while True:
        if player == "a":
            if len(da) == 0:
                print("A")
                exit()

            player = da.popleft()

        elif player == "b":
            if len(db) == 0:
                print("B")
                exit()

            player = db.popleft()
        else:
            if len(dc) == 0:
                print("C")
                exit()

            player = dc.popleft()


if __name__ == "__main__":
    main()
