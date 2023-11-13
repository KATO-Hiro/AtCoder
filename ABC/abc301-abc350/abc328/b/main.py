# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    d = list(map(int, input().split()))
    ans = 0

    for i, di in enumerate(d, 1):
        for j in range(1, di + 1):
            t = set()

            for ii in list(str(i)):
                t.add(ii)

            for jj in list(str(j)):
                t.add(jj)

            if len(t) == 1:
                # print(i, j, t)
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
