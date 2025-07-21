# -*- coding: utf-8 -*-

def solve():
    n = int(input())
    s = input().rstrip()
    n2 = 1 << n
    visited = [False] * n2
    visited[0] = True

    for bit in range(n2):
        if not visited[bit]:
            continue

        for i in range(n):
            ni = bit | (1 << i)

            if ni == bit:
                continue
            if s[ni - 1] == "1":
                continue

            visited[ni] = True
            
    if visited[n2 - 1]:
        print("Yes")
    else:
        print("No")


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
