# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x, y = map(int, input().split())
    grid_max = 10 ** 4
    x += grid_max
    y += grid_max

    a = list(map(int, input().split()))
    ax = list()
    ay = list()

    for i, ai in enumerate(a):
        if i % 2 == 0:
            ax.append(ai)
        else:
            ay.append(ai)
    
    axis_max = 2 * grid_max + 1
    dp_x = [False] * axis_max
    dp_x[ax[0] + grid_max] = True
    dp_y = [False] * axis_max
    dp_y[ay[0] + grid_max] = True
    dp_y[-ay[0] + grid_max] = True

    for axi in ax[1:]:
        ndp_x = [False] * axis_max

        for i in range(axis_max):
            if dp_x[i]:
                if i + axi < axis_max:
                    ndp_x[i + axi] = True 
                if 0 <= i - axi:
                    ndp_x[i - axi] = True 

        dp_x = ndp_x

    for ayi in ay[1:]:
        ndp_y = [False] * axis_max

        for i in range(axis_max):
            if dp_y[i]:
                if i + ayi < axis_max:
                    ndp_y[i + ayi] = True 
                if 0 <= i - ayi:
                    ndp_y[i - ayi] = True 

        dp_y = ndp_y
    
    if dp_x[x] and dp_y[y]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
