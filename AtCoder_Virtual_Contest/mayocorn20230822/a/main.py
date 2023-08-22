# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    s = input().rstrip()
    ans = list()

    for si in s:
        if si == "o":
            if k > 0:
                k -= 1
                ans.append(si)
            else:
                ans.append("x")
        else:
            ans.append(si)

    print("".join(ans))


if __name__ == "__main__":
    main()
