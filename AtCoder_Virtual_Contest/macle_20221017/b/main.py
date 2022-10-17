# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    q = int(input())
    d = deque()

    for i in range(q):
        qi = list(map(int, input().split()))

        if qi[0] == 1:
            xi, ci = qi[1], qi[2]
            
            if len(d) > 0 and d[-1][0] == xi:
                dj, cj = d.pop()
                d.append((dj, cj + ci))
            else:
                d.append((xi, ci))
        else:
            ci = qi[1]
            summed = 0

            while ci > 0:
                dj, cj = d.popleft() 
                c_min = min(ci, cj)
                summed += c_min * dj

                ci -= cj

                if cj > c_min:
                    d.appendleft((dj ,cj - c_min))
        
            print(summed)


if __name__ == "__main__":
    main()
