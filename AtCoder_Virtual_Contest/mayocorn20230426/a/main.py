# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    angles = set()
    angles.add(0)
    angles.add(360)
    angle = 0

    for ai in a:
        angle += ai
        angle %= 360
        angles.add(angle)
    
    angles = sorted(angles)
    ans = 0

    for i, j in zip(angles, angles[1:]):
        ans = max(ans, j - i)
    
    print(ans)


if __name__ == "__main__":
    main()
