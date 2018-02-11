# -*- coding: utf-8 -*-

# AtCoder Beginner Contest 001
# Problem B
# Report of visibility.


def toVV(length_m: int):
    length_km = length_m / 1000

    if length_km < 0.1:
        return "00"
    elif 0.1 <= length_km < 1:
        raw_VV = int(length_km * 10)
        return "0" + str(raw_VV)
    elif 1 <= length_km <= 5:
        return str(int(length_km * 10))
    elif 6 <= length_km <= 30:
        return str(int(length_km + 50))
    elif 35 <= length_km <= 70:
        return str(int(((length_km - 30) / 5) + 80))
    elif length_km > 70:
        return "89"


if __name__ == '__main__':
    length_m = int(input())
    result = toVV(length_m)
    print(result)
