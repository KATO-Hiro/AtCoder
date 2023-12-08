# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    m0, d0 = map(int, input().split())
    y1, m1, d1 = map(int, input().split())

    dm, d_dash = divmod(d1 + 1, d0)

    if d_dash == 0:
        dm -= 1
        d_dash = d0

    dy, m_dash = divmod(m1 + dm, m0)

    if m_dash == 0:
        dy -= 1
        m_dash = m0

    y_dash = y1 + dy

    print(y_dash, m_dash, d_dash)


if __name__ == "__main__":
    main()
