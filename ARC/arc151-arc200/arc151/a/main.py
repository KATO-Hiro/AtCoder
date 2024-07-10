# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    t = input().rstrip()
    count = 0
    pos_s, pos_t = list(), list()

    for i, (si, ti) in enumerate(zip(s, t)):
        if si != ti:
            count += 1

            if si == "1":
                pos_s.append(i)
            else:
                pos_t.append(i)

    if count % 2 == 1:
        print(-1)
        exit()

    size_pos_s, size_pos_t = len(pos_s), len(pos_t)
    ans = ["0"] * n

    if size_pos_s > size_pos_t:
        d = (size_pos_s - size_pos_t) // 2

        for i in pos_s[-d:]:
            ans[i] = "1"
    elif size_pos_s < size_pos_t:
        d = (size_pos_t - size_pos_s) // 2

        for i in pos_t[-d:]:
            ans[i] = "1"

    print("".join(ans))


if __name__ == "__main__":
    main()
