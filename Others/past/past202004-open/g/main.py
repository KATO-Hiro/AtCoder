# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict, deque

    input = sys.stdin.readline

    q = int(input())
    que = deque()

    for _ in range(q):
        qi = input().rstrip().split()

        if qi[0] == "1":
            ci, xi = qi[1:]
            que.append((ci, int(xi)))
        else:
            di = int(qi[1])
            dd = defaultdict(int)

            while que:
                ci, xi = que.popleft()
                diff = xi - di

                if diff >= 0:
                    dd[ci] += di

                    if diff > 0:
                        que.appendleft((ci, diff))

                    break
                else:
                    di -= xi
                    dd[ci] += xi

            ans = 0

            for value in dd.values():
                ans += value**2

            print(ans)


if __name__ == "__main__":
    main()
