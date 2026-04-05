# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    m = int(input())
    s = [list(input().rstrip()) for _ in range(m)]
    t = set()

    for ai, bi in ab:
        for si in s:
            if len(si) != ai:
                continue

            sij = si[bi - 1]
            t.add((ai, bi, sij))

    ans = []

    for si in s:
        if len(si) != n:
            ans.append("No")
            continue

        ok = True

        for (ai, bi), sij in zip(ab, si):
            if (ai, bi, sij) not in t:
                ok = False
                break

        if ok:
            ans.append("Yes")
        else:
            ans.append("No")

    print("\n".join(ans))


if __name__ == "__main__":
    main()
