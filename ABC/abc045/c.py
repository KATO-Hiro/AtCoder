'''input
5
5

125
176

9999999999
12656242944

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C


def dfs(i: int):
    global count

    if i == n - 1:
        count += eval(''.join(numbers))
        return

    numbers[2 * i + 1] = ""
    dfs(i + 1)
    numbers[2 * i + 1] = "+"
    dfs(i + 1)


if __name__ == '__main__':
    s = input()
    n = len(s)
    numbers = [""] * (2 * n - 1)
    count = 0

    for i in range(n):
        numbers[2 * i] = s[i]

    dfs(0)
    print(count)
