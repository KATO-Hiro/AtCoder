# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    left = deque()
    rem = set()
    count = 0

    for i, si in enumerate(s):
        if si == "(":
            left.append((i, si))
            count += 1
        elif si == ")":
            while len(left) > 0 and count > 0:
                j, sj = left.pop()

                if sj == "(":
                    rem.add(j)
                    rem.add(i)
                    count -= 1
                    break
                else:
                    rem.add(j)
        else:
            left.append((i, si))
        # print(left)

    rem = set(rem)
    ans = list()

    for i, si in enumerate(s):
        if i not in rem:
            ans.append(si)

    print("".join(ans))


if __name__ == "__main__":
    main()
