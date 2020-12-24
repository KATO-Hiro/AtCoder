# -*- coding: utf-8 -*-


# See:
# https://atcoder.jp/contests/past202004-open/submissions/12572084
def calc(si):
    ni = len(si)
    results = set()

    for i in range(1 << ni):
        t = ""

        for j in range(ni):
            if i >> j & 1:
                t += si[j]
            else:
                t += "."

        results.add(t)

    return results


def main():
    s = input()
    n = len(s)
    strings = set()

    for i in range(n):
        for j in range(1, 3 + 1):
            si = s[i : i + j]

            for c in calc(si):
                strings.add(c)

    print(len(strings))


if __name__ == "__main__":
    main()
