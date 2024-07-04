# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    r_id, m_id = 0, 0

    for i, si in enumerate(s):
        if si == "R":
            r_id = i
        elif si == "M":
            m_id = i

    if r_id < m_id:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
