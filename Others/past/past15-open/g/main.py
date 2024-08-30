# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    conditions = []

    # See:
    # https://atcoder.jp/contests/past15-open/submissions/47842986
    for _ in range(m):
        ki = int(input())
        ab = [tuple(map(int, input().split())) for _ in range(ki)]
        conditions.append(ab)

    for bit in range(1 << n):
        for condition in conditions:
            ok = False

            for ai, bi in condition:
                ai -= 1

                if (bit >> ai) & 1 == bi:
                    ok = True
                    break

            if not ok:
                break
        else:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
