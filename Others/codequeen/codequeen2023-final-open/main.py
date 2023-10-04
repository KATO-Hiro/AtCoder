# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    e = input().rstrip()
    ans = list()

    for si in s:
        if si == e:
            ans.append(si)
            ans.append(si)
        else:
            ans.append(si)

    print("".join(ans))


if __name__ == "__main__":
    main()
