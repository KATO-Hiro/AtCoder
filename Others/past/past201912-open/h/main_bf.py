# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    c = list(map(int, input().split()))
    q = int(input())
    ans = 0

    for _ in range(q):
        si = list(map(int, input().split()))

        if si[0] == 1:
            xi, ai = si[1:]
            xi -= 1

            if c[xi] >= ai:
                c[xi] -= ai
                ans += ai
        elif si[0] == 2:
            ai = si[1]
            count = [1 for i, ci in enumerate(c) if (i % 2 == 0) and ci < ai]

            if sum(count) == 0:
                for i in range(n):
                    if i % 2 == 0:
                        c[i] -= ai
                        ans += ai
        else:
            ai = si[1]

            if min(c) >= ai:
                for i in range(n):
                    c[i] -= ai
                    ans += ai

        print(ans)
    print(ans)


if __name__ == "__main__":
    main()
