# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    c = list(map(int, input().split()))
    s = [set([ci]) for ci in c]
    # print(s)

    # マージテク
    for _ in range(q):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        if len(s[ai]) > len(s[bi]):
            s[ai], s[bi] = s[bi], s[ai]

        for sai in s[ai]:
            s[bi].add(sai)

        s[ai] = set()

        print(len(s[bi]))


if __name__ == "__main__":
    main()
