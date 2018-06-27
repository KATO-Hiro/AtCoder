'''input
1000
972926972

3
4

6
30

1

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C


# See:
# https://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%A9%E3%83%88%E3%82%B9%E3%83%86%E3%83%8D%E3%82%B9%E3%81%AE%E7%AF%A9
def get_prime_dict(number: int) -> dict:
    ''' number: 2 or greater.
    '''
    from collections import OrderedDict
    from math import sqrt

    prime_dict = OrderedDict()
    j = 2
    prime_dict[j] = 0
    number_list = [int(i) for i in range(2, number + 1)]

    while number_list[0] <= int(sqrt(number)):
        for i in number_list:
            if i % j == 0:
                number_list.remove(i)

        j = number_list[0]
        prime_dict[j] = 0

    for prime in number_list:
        prime_dict[prime] = 0

    return prime_dict


def execute_prime_factorization(primes: dict, number: int):
    for key in primes.keys():
        if number >= key:
            tmp = number

            while tmp >= key:
                if tmp % key == 0:
                    primes[key] += 1
                    tmp = int(tmp / key)
                else:
                    break
    return primes


if __name__ == '__main__':
    number = int(input())

    if number == 1:
        print(1)
        exit()

    # See:
    # https://atcoder.jp/img/arc067/editorial.pdf
    primes = get_prime_dict(number)
    count = 1

    for i in range(2, number + 1):
        execute_prime_factorization(primes, i)

    for value in primes.values():
        count = ((value + 1) * count) % (10 ** 9 + 7)

    print(count)
