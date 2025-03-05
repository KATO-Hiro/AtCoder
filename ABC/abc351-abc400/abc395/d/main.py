# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())

    # 鳩p、袋b、巣h
    p2b = [i for i in range(n)]
    b2h = [i for i in range(n)]
    h2b = [i for i in range(n)]

    for _ in range(q):
        qi = list(map(int, input().split()))

        if qi[0] == 1:
            ai, bi = qi[1:]
            ai -= 1
            bi -= 1

            p2b[ai] = h2b[bi]
        elif qi[0] == 2:
            ai, bi = qi[1:]
            ai -= 1
            bi -= 1

            h2b[ai], h2b[bi] = h2b[bi], h2b[ai]
            b2h[h2b[ai]] = ai
            b2h[h2b[bi]] = bi
        else:
            ai = qi[1]
            ai -= 1

            ans = b2h[p2b[ai]]
            print(ans + 1)


if __name__ == "__main__":
    main()
