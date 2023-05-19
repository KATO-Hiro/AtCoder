# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import combinations_with_replacement, permutations

    input = sys.stdin.readline

    s = input().rstrip()

    if s.count("o") > 4 or (s.count("x") > 6 and s.count("?") == 0):
        print(0)
        exit()

    dot = [i for i, si in enumerate(s) if si == ("o")]
    dot_count = len(dot)
    q = [i for i, si in enumerate(s) if si == ("?")]
    ans = set()

    # 最大でも10 ** 4通りのはず
    for pattern in combinations_with_replacement(dot + q, 4 - dot_count):
        for p in permutations(list(pattern) + dot):
            ans.add(p)

    print(len(ans))


if __name__ == "__main__":
    main()
