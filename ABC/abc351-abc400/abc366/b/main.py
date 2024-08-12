# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = [list(input().rstrip()) for _ in range(n)]
    m = max([len(si) for si in s])
    u = list()

    # m未満の場合は、不足分を"*"で埋める
    for si in s:
        si += ["*"] * (m - len(si))
        u.append(si)

    for ti in zip(*u):
        ti = list(ti[::-1])

        while ti and ti[-1] == "*":
            ti.pop()

        print("".join(ti))


if __name__ == "__main__":
    main()
