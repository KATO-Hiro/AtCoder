# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    ok = True
    ans = []

    for si in s:
        if ok and si == "o":
            continue
        else:
            ok = False
            ans.append(si)

    print("".join(ans))


if __name__ == "__main__":
    main()
