# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    t = input().rstrip()
    n, m = len(s), len(t)
    ans = list()

    for i in range(n):
        if i + m > n:
            break

        tmp = s[i : i + m]
        flag = True

        for sij, tij in zip(tmp, t):
            if sij != "?" and sij != tij:
                flag = False
                break

        if not flag:
            continue

        u = s
        u1, u2 = u[:i], u[i + m :]

        if len(u1) > 0:
            u1 = u1.replace("?", "a")
        if len(u2) > 0:
            u2 = u2.replace("?", "a")

        ans.append("".join(u1 + t + u2))

    if len(ans) == 0:
        print("UNRESTORABLE")
    else:
        print(sorted(ans)[0])


if __name__ == "__main__":
    main()
