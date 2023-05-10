# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n, q = map(int, input().split())

    front = [-1] * (n + 1)
    back = [-1] * (n + 1)

    for _ in range(q):
        qi = list(map(int, input().split()))

        if qi[0] == 1:
            x, y = qi[1:]
            back[x], front[y] = y, x
        elif qi[0] == 2:
            x, y = qi[1:]
            back[x], front[y] = -1, -1

        else:
            x = qi[1]
            i = x
            ans = deque()

            # iよりも前のidを探す
            while True:
                i = front[i]

                if i == -1:
                    break

                ans.appendleft(i)

            ans.append(x)
            i = x

            # iよりも後のidを探す
            while True:
                i = back[i]

                if i == -1:
                    break

                ans.append(i)

            ans = list(ans)
            print(*[len(ans)] + ans)


if __name__ == "__main__":
    main()
