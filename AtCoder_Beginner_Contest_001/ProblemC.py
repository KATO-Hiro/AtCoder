# -*- coding: utf-8 -*-

# AtCoder Beginner Contest 001
# Problem C
# Observation of wind speed.


def to_direction(degree):
    direction_symbols = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                         "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]

    number = int(((degree * 10 + 1125) / 2250) % 16)
    return direction_symbols[number]


def to_beaufort_wind_class(run_meter_per_minute):
    boundary_values = [0, 15, 93, 201, 327, 477, 645, 831, 1029, 1245, 1467,
                       1707, 1959, 12000]

    for level in range(0, 13):
        if boundary_values[level] <= run_meter_per_minute < boundary_values[level + 1]:
            return level


def is_no_wind(beaufort_wind_class):
    if beaufort_wind_class == 0:
        return True
    else:
        return False


def my_round(value, display_digit=0):
    '''Rounds to arbitrary decimal places.
    '''
    ratio = 10 ** display_digit
    return (value * ratio * 2 + 1) // 2 / ratio


if __name__ == '__main__':
    # Input
    wind_degree, wind_run_meter_per_minute = input().split(" ")

    # Convert to wind run
    wind_strength = to_beaufort_wind_class(int(wind_run_meter_per_minute))

    # Convert to direction
    if is_no_wind(wind_strength):
        wind_direction = "C"
    else:
        wind_direction = to_direction(int(wind_degree))

    # Output
    print(wind_direction + " " + str(wind_strength))
