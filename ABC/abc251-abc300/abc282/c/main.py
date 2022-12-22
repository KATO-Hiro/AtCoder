# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = list(input().rstrip())
    count = 0
    ans = list()

    for si in s:
        if si == '"':
            count += 1

        if si == "," and count % 2 == 0:
            ans.append(".")
        else:
            ans.append(si)
    
    print("".join(ans))
    

if __name__ == "__main__":
    main()
