# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = list(input().rstrip())
    maru = [0 for _ in range(n + 1)]
    batsu = [0 for _ in range(n + 1)]
    ans = 0

    for index, si in enumerate(s, 1):
        maru[index] = maru[index - 1]
        batsu[index] = batsu[index - 1]

        if si == "o":
            maru[index] = index
            batsu[index] = batsu[index - 1]
        else:
            maru[index] = maru[index - 1]
            batsu[index] = index
        
        ans += min(maru[index], batsu[index])
    
    print(ans)


if __name__ == "__main__":
    main()
