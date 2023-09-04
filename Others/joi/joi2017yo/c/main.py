# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w, d = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(h)]
    ans = 0

    # 全探索
    for i in range(h):
        for j in range(w):
            if j + d - 1 >= w:
                break

            ok = True

            for k in range(j, j + d):
                if s[i][k] == "#":
                    ok = False
                    break

            if ok:
                ans += 1

    for j in range(w):
        for i in range(h):
            if i + d - 1 >= h:
                break

            ok = True

            for k in range(i, i + d):
                if s[k][j] == "#":
                    ok = False
                    break

            if ok:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
