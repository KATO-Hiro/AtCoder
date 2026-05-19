# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    t = input().rstrip()
    ans = []

    for si, ti in zip(s, t):
        if si == ti:
            ans.append(si)
            continue
        elif si == "?":
            ans.append(ti)
            continue
        elif ti == "?":
            ans.append(si)
            continue
        else:
            ans.append("!")

    print("".join(ans))

    if "!" in ans:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
