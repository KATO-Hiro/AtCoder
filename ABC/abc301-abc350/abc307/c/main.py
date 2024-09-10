# -*- coding: utf-8 -*-


def find_black_pos(h):
    pos = []

    for i in range(h):
        si = input().rstrip()

        for j, sij in enumerate(si):
            if sij == "#":
                pos.append((i, j))

    return pos


def main():
    import sys

    input = sys.stdin.readline

    ha, wa = map(int, input().split())
    black_pos_a = find_black_pos(ha)

    hb, wb = map(int, input().split())
    black_pos_b = find_black_pos(hb)

    hx, wx = map(int, input().split())
    black_pos_x = set(find_black_pos(hx))

    def f(i, j, sheet):
        ok = True
        candidates = []

        for si, sj in sheet:
            ni, nj = i + si, j + sj

            if not (0 <= ni < hx and 0 <= nj < wx):
                ok = False
                break
            if not (ni, nj) in black_pos_x:
                ok = False
                break

            candidates.append((ni, nj))

        return ok, candidates

    a_count, b_count = 0, 0
    remains = set(black_pos_x)

    for i in range(-hx, hx):
        for j in range(-wx, wx):
            ok, candidates_a = f(i, j, black_pos_a)

            if ok:
                a_count += 1
                remains -= set(candidates_a)

            ok, candidates_b = f(i, j, black_pos_b)

            if ok:
                b_count += 1
                remains -= set(candidates_b)

    if len(remains) == 0 and a_count >= 1 and b_count >= 1:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
