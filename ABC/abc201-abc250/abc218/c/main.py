# -*- coding: utf-8 -*-


def read_grid(n):
    sharps = set()

    for x in range(n):
        line = input()

        for y in range(n):
            if line[y] == '#':
                sharps.add((x, y))
    
    return sharps


def main():
    n = int(input())
    s = read_grid(n)
    t = read_grid(n)

    for _ in range(4):
        x_min, y_min = min(s)
        s = set((x - x_min, y - y_min) for x, y in s)
        x_min, y_min = min(t)
        t = set((x - x_min, y - y_min) for x, y in t)

        if s == t:
            print("Yes")
            exit()
        
        t = set((y, -x) for x, y in t)
    
    print("No")


if __name__ == "__main__":
    main()
