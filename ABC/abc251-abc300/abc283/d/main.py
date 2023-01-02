# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    box = set()
    stack = [[]]

    for i, si in enumerate(s):
        if si == "(":
            stack.append([])
            pass
        elif si == ")":
            for ci in stack.pop():
                box.discard(ci)
        else:
            if si not in box:
                box.add(si)
                stack[-1].append(si)
            else:
                print("No")
                exit()
    
    print("Yes")
    

if __name__ == "__main__":
    main()
