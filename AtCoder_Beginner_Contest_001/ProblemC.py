# -*- coding: utf-8 -*-

# AtCoder Beginner Contest 001
# Problem C
# Observation of wind speed.


def to_direction(degree):
    if 11.25 <= degree < 33.75:
        return "NNE"
    elif 33.75 <= degree < 56.25:
        return "NE"
    elif 56.25 <= degree < 78.75:
        return "ENE"
    elif 78.75 <= degree < 101.25:
        return "E"
    elif 101.25 <= degree < 123.75:
        return "ESE"
    elif 123.75 <= degree < 146.25:
        return "SE"
    elif 146.25 <= degree < 168.75:
        return "SSE"
    elif 168.75 <= degree < 191.25:
        return "S"
    elif 191.25 <= degree < 213.75:
        return "SSW"
    elif 213.75 <= degree < 236.25:
        return "SW"
    elif 236.25 <= degree < 258.75:
        return "WSW"
    elif 258.75 <= degree < 281.25:
        return "W"
    elif 281.25 <= degree < 303.75:
        return "WNW"
    elif 303.75 <= degree < 326.25:
        return "NW"
    elif 326.25 <= degree < 348.75:
        return "NNW"
    else:
        return "N"


def to_beaufort_wind_class(wind_speed):
    if 0.0 <= wind_speed <= 0.2:
        return 0
    elif 0.3 <= wind_speed <= 1.5:
        return 1
    elif 1.6 <= wind_speed <= 3.3:
        return 2
    elif 3.4 <= wind_speed <= 5.4:
        return 3
    elif 5.5 <= wind_speed <= 7.9:
        return 4
    elif 8.0 <= wind_speed <= 10.7:
        return 5
    elif 10.8 <= wind_speed <= 13.8:
        return 6
    elif 13.9 <= wind_speed <= 17.1:
        return 7
    elif 17.2 <= wind_speed <= 20.7:
        return 8
    elif 20.8 <= wind_speed <= 24.4:
        return 9
    elif 24.5 <= wind_speed <= 28.4:
        return 10
    elif 28.5 <= wind_speed <= 32.6:
        return 11
    elif 32.7 >= wind_speed:
        return 12


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

    # convert to wind run
    wind_speed = my_round(float(int(wind_run_meter_per_minute) / 60), 1)
    wind_strength = to_beaufort_wind_class(wind_speed)

    # convert to direction
    if is_no_wind(wind_strength):
        wind_direction = "C"
    else:
        wind_direction = to_direction(float(wind_degree) / 10)

    # Output
    print(wind_direction + " " + str(wind_strength))
