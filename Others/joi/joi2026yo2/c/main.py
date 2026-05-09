# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    stack = []

    for si in s:
        stack.append(si)

        if len(stack) >= 2 and stack[-2] == "O" and stack[-1] == "I":
            for _ in range(2):
                stack.pop()

            stack.append("Z")

    ans = []
    tmp = []

    for sj in stack:
        if sj == "J" or sj == "Z":
            tmp.append(sj)
        else:
            tmp.sort(reverse=True)

            for tmp_i in tmp:
                if tmp_i == "J":
                    ans.append(tmp_i)
                else:
                    ans.append("O")
                    ans.append("I")

            ans += [sj]
            tmp = []

    if len(tmp) >= 1:
        tmp.sort(reverse=True)

        for tmp_i in tmp:
            if tmp_i == "J":
                ans.append(tmp_i)
            else:
                ans.append("O")
                ans.append("I")

    print("".join(ans))


if __name__ == "__main__":
    main()
