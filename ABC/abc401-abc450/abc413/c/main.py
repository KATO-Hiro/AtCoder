# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    q = int(input())
    d = deque()

    for _ in range(q):
        query = list(map(int, input().split()))

        if query[0] == 1:
            ci, xi = query[1:]
            d.append((xi, ci))
        else:
            k = query[1]
            remain = k
            ans = 0

            while d and remain > 0:
                yi, count = d.popleft()

                if count >= remain:
                    ans += yi * remain
                    d.appendleft((yi, count - remain))
                    break
                else:
                    ans += yi * count
                    remain -= count

            print(ans)


if __name__ == "__main__":
    main()
