# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    s = []
    s.append(["."] * (w + 2))

    for _ in range(h):
        si = list(input().rstrip())
        s.append(["."] + si + ["."])

    s.append(["."] * (w + 2))
    ans = 0

    for h1 in range(1, h + 1):
        for h2 in range(h1, h + 1):
            for w1 in range(1, w + 1):
                for w2 in range(w1, w + 1):
                    ok = True

                    for i in range(h1, h2 + 1):
                        for j in range(w1, w2 + 1):
                            if s[i][j] != s[h1 + h2 - i][w1 + w2 - j]:
                                ok = False
                                break

                    if ok:
                        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
