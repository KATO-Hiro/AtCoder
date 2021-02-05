# -*- coding: utf-8 -*-


def main():
    from collections import deque

    n = int(input())
    d = deque()

    for i in range(n):
        si = input()

        if si == "A":
            d.append(si)
        else:
            if len(d) > 0:
                d.popleft()
            else:
                print("NO")
                exit()

    if len(d) > 0:
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    main()
