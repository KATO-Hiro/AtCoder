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
# https://beta.atcoder.jp/contests/abc052/submissions/2246922
def get_prime_dict(number: int) -> dict:
    ''' number: 2 or greater.
    '''
    from collections import OrderedDict

    prime_dict = OrderedDict()
    j = 2
    prime_dict[j] = 0

    for i in range(2, number + 1):
        if all(i % j != 0 for j in prime_dict.keys()):
            prime_dict[i] = 0
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
