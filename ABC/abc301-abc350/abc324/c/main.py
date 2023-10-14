# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, t_dash = input().rstrip().split()
    m = len(t_dash)
    n = int(n)
    ans = list()

    for i in range(1, n + 1):
        si = input().rstrip()
        u = len(si)

        if abs(u - m) > 2:
            continue

        if u == m:
            count = 0

            for ti, sij in zip(t_dash, si):
                if ti != sij:
                    count += 1

            if count <= 1:
                ans.append(i)
        else:
            if m > u:
                pos = 0

                for x, (ti, sij) in enumerate(zip(t_dash, si)):
                    if ti != sij:
                        pos = x
                        break

                if t_dash[pos + 1 :] == si[pos:]:
                    ans.append(i)
                elif t_dash[1:] == si:
                    ans.append(i)
                elif t_dash[:-1] == si:
                    ans.append(i)
            else:
                pos = 0

                for x, (ti, sij) in enumerate(zip(t_dash, si)):
                    if ti != sij:
                        pos = x
                        break

                if t_dash[pos:] == si[pos + 1 :]:
                    ans.append(i)
                elif t_dash == si[1:]:
                    ans.append(i)
                elif t_dash == si[:-1]:
                    ans.append(i)

    print(len(set(ans)))

    if len(ans) > 0:
        print(*sorted(set(ans)))


if __name__ == "__main__":
    main()
