# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w, n = map(int, input().split())
    hw = []

    for i in range(n):
        hi, wi = map(int, input().split())
        hw.append((hi, wi, i))

    hw1 = sorted(hw)
    hw2 = sorted(hw, key=lambda x: (x[1], x[0]))
    used = set()
    pending = -1
    ans = [(pending, pending)] * n
    y, x = 1, 1

    while hw1 and hw2:
        if hw1[-1][0] == h:
            h1, w1, id1 = hw1.pop()
            ans[id1] = (y, x)

            x += w1
            w -= w1
            used.add(id1)
        elif hw2[-1][1] == w:
            h2, w2, id2 = hw2.pop()
            ans[id2] = (y, x)

            y += h2
            h -= h2
            used.add(id2)

        while hw1 and hw1[-1][-1] in used:
            hw1.pop()

        while hw2 and hw2[-1][-1] in used:
            hw2.pop()

    for ans_i in ans:
        print(*ans_i)


if __name__ == "__main__":
    main()
