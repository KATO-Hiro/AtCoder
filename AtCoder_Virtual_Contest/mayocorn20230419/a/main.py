# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    xyz = list(map(int, input().split())) 
    plus_count = 0

    for i in xyz:
        if i > 0:
            plus_count += 1
        
    x, y, z = xyz[0], xyz[1], xyz[2]
    ans = abs(x)
    
    if plus_count == 3:
        if min(xyz) == y:
            ans = -1
    elif plus_count == 2:
        if z < y < x:
            ans = abs(x) + abs(2 * z)
    elif plus_count == 1:
        if x < y < z:
            ans = abs(x) + abs(2 * z)
    else:
        if max(xyz) == y:
            ans = -1

    print(ans)


if __name__ == "__main__":
    main()
