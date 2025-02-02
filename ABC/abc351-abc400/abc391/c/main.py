# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    ps = [i for i in range(n)]
    hs = [1 for _ in range(n)]
    count = 0

    for _ in range(q):
        query = list(map(int, input().split()))

        if query[0] == 1:
            pi, hi = query[1:]
            pi -= 1
            hi -= 1

            cur = ps[pi]

            if hs[cur] == 2:
                count -= 1

            hs[cur] -= 1

            ps[pi] = hi
            next = ps[pi]

            if hs[next] == 1:
                count += 1

            hs[next] += 1
        else:
            print(count)


if __name__ == "__main__":
    main()
