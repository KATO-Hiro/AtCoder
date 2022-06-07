# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    n, x, y = map(int, input().split())
    a = list(map(int, input().split())) * 2
    summed_a = sum(a) // 2
    d = deque()

    total = 0

    # Two-Pointer Technique using deque.
    # See:
    # https://qiita.com/keroru/items/6e0a22e8c9bf2a24dc68
    for ai in a:
        d.append(ai)
        total += ai

        while d and total > x:
            di = d.popleft()
            total -= di
        
        if (total == x) and (summed_a - x == y):
            print("Yes")
            exit()
    
    print("No")


if __name__ == "__main__":
    main()
