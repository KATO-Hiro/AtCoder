# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    dp_x = set([a[0]])
    dp_y = set([0])

    for i in range(2, n, 2):
        ndp_x = set()

        for dp_xi in dp_x:
            ndp_x.add(dp_xi + a[i])
            ndp_x.add(dp_xi - a[i])
        
        dp_x = ndp_x

    for j in range(1, n, 2):
        ndp_y = set()

        for dp_yi in dp_y:
            ndp_y.add(dp_yi + a[j])
            ndp_y.add(dp_yi - a[j])
        
        dp_y = ndp_y
    
    if (x in dp_x) and (y in dp_y):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
