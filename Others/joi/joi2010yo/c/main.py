# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    m = int(input())
    friends = [[] for _ in range(n)]

    for i in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        friends[ai].append(bi)
        friends[bi].append(ai)

    ans = set()

    for f in friends[0]:
        ans.add(f)

    for f in friends[0]:
        for fi in friends[f]:
            if fi != 0:
                ans.add(fi)

    print(len(ans))


if __name__ == '__main__':
    main()
