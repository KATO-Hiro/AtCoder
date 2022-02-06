# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline
    
    s = input().rstrip()
    n = len(s)
    left_count, right_count = 0, 0

    for si in s:
        if si == "a":
            left_count += 1
        else:
            break

    for si in reversed(s):
        if si == "a":
            right_count += 1
        else:
            break
    
    diff = right_count - left_count

    if diff > 0:
        s = "a" * diff + s
    
    if s == s[::-1]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
