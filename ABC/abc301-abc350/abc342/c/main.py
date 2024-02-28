# -*- coding: utf-8 -*-


def main():
    import sys
    from string import ascii_lowercase

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    q = int(input())
    d = {si: si for si in ascii_lowercase}

    for _ in range(q):
        ci, di = input().rstrip().split()

        for key, value in d.items():
            if value == ci:
                d[key] = di

    ans = list()

    for si in s:
        ans.append(d[si])

    print("".join(ans))


if __name__ == "__main__":
    main()
