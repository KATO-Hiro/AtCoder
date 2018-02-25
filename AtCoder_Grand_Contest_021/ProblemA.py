# -*- coding: utf-8 -*-

# AtCoder Grand Contest
# Problem A


def get_most_significant_digit(number: int):
    separated_number = list(map(int, str(number)))
    return separated_number[0]


def count_digit(number: int):
    return len(str(number))


def generate_candidate_value(most_significant_digit, digit_count):
    filled_with_9 = 10 ** (digit_count - 1) - 1

    if digit_count > 1:
        candidate_value = str(most_significant_digit) + str(filled_with_9)
    else:
        candidate_value = str(most_significant_digit)
    return int(candidate_value)


def sum_digit(number: int, candidate_value: int):
    result = sum(list(map(int, str(candidate_value))))

    if number >= candidate_value:
        return result
    else:
        return result - 1


if __name__ == '__main__':
    number = int(input())

    # See: https://img.atcoder.jp/agc021/editorial.pdf
    most_significant_digit = get_most_significant_digit(number)
    digit_count = count_digit(number)
    candidate_value = generate_candidate_value(most_significant_digit,
                                               digit_count)

    result = sum_digit(number, candidate_value)
    print(result)
