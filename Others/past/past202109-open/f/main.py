# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = input()
    zero_count = s.count('0')

    if zero_count == 1:
        print(-1)
        exit()

    ans = [i for i in range(1, n + 1)]
    indices = list()
    numbers = list()

    for index, si in enumerate(s):
        if si == '0':
            indices.append(index)
            numbers.append(index + 1)
    
    if len(numbers) >= 2:
        for index, number in zip(indices, numbers[1:] + [numbers[0]]):
            ans[index] = number

    print(' '.join(map(str, ans)))


if __name__ == "__main__":
    main()
