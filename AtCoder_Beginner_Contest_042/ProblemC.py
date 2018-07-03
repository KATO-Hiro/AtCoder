'''input
9999 1
0
9999

1000 8
1 3 4 5 6 7 8 9
2000

9999 1
9
10000

9999 9
0 1 3 4 5 6 7 8 9
22222

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    n, k = list(map(str, input().split()))
    d = list(map(str, input().split()))
    numbers = [str(i) for i in range(0, 10)]
    like_numbers = sorted(set(numbers) - set(d))

    for i in like_numbers:
        for j in like_numbers:
            for k in like_numbers:
                for l in like_numbers:
                    for m in like_numbers:
                        number_candidate = i + j + k + l + m

                        if int(number_candidate) >= int(n):
                            print(int(number_candidate))
                            exit()
