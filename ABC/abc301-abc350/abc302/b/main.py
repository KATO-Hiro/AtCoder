# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    s = [input().rstrip() for _ in range(h)]
    dyx = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    t = "snuke"

    for dy, dx in dyx:
        for i in range(h):
            for j in range(w):
                u = list()
                candidate = list()

                for k in range(5):
                    nx = j + dx * k
                    ny = i + dy * k

                    if not (0 <= nx < w):
                        continue
                    if not (0 <= ny < h):
                        continue

                    u.append(s[ny][nx])
                    candidate.append((ny + 1, nx + 1))

                if len(u) != 5:
                    continue

                if "".join(u) == t:
                    for ri, ci in candidate:
                        print(ri, ci)

                    exit()


if __name__ == "__main__":
    main()
