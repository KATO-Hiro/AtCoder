'''input
4
3
4
1
2

-1

5
3
3
4
2
4

3

3
3
1
2

2

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    button_count = int(input())
    button_rules = {i + 1: int(input()) for i in range(button_count)}

    count = 1
    result = button_rules[count]

    # HACK: More smarter.
    while (result != 2) and (count < 10 ** 5):
        result = button_rules[result]
        count += 1

    if count < 10 ** 5:
        print(count)
    else:
        print(-1)
