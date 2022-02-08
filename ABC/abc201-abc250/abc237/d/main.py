# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()

    tmp = 5 * 10 ** 5 + 10
    left = [tmp] * (n + 1)
    right = [tmp] * (n + 1)

    for i, si in enumerate(s, 1):
        if si == "L":
            x = left[i - 1]
            left[i - 1] = i
            right[i] = i - 1

            if x != tmp:
                left[i] = x
                right[x] = i
        else:
            y = right[i - 1]
            right[i - 1] = i
            left[i] = i - 1

            if y != tmp:
                right[i] = y
                left[y] = i
    
    old_id = left.index(tmp)
    ans = [old_id]

    for i in range(n):
        new_id = right[old_id]
        ans.append(new_id)
        old_id = new_id
    
    print(*ans)


if __name__ == "__main__":
    main()
