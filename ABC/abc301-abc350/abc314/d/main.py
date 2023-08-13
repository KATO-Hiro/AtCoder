# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = list(input().rstrip())
    q = int(input())
    status = -1  # 0: small, 1: large
    tmp = list()

    for _ in range(q):
        qi = input().rstrip().split()

        if qi[0] == "1":
            xi, ci = int(qi[1]) - 1, qi[2]
            s[xi] = ci

            if ci.islower():
                t = 0
            else:
                t = 1

            tmp.append((xi, t))
        elif qi[0] == "2":
            tmp = list()
            status = 0
        else:
            tmp = list()
            status = 1

    # print(tmp)
    ans = list()

    if status == -1:
        print("".join(s))
    elif status == 0:
        for si in s:
            ans.append(si.lower())

        if len(tmp) > 0:
            for id, flag in tmp:
                if flag == 1:
                    ans[id] = ans[id].upper()

        print("".join(ans))
    else:
        for si in s:
            ans.append(si.upper())

        if len(tmp) > 0:
            for id, flag in tmp:
                if flag == 0:
                    ans[id] = ans[id].lower()

        print("".join(ans))


if __name__ == "__main__":
    main()
