'''input
55


6
2 3 5 7 11 13

8
2 5 7 13 19 37 67 79

5
3 5 7 11 31

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem D


if __name__ == '__main__':
    n = int(input())
    x = [2]

    for i in range(2, 2000 + 1):
        if all(i % j != 0 for j in x):
            x.append(i)

    # https://www.youtube.com/watch?v=geZKa28g93o
    primes = [xi for xi in x if (xi % 5 == 1) and (xi >= 10)]
    print(' '.join(map(str, primes[:n])))
