'''input
2
5 1 1
100 1 1
'''

'''
2
3 1 2
6 1 1
'Yes'
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C


class TravelingPlan(object):

    def __init__(self):
        from collections import OrderedDict
        self._points = OrderedDict()

    def add_point(self, name: str):
        if name not in self._points:
            self._points[name] = Point()
        return self._points[name]

    def is_executable(self):
        for j in range(len(self._points) - 1):
            current_point = self._points[str(j + 1)]
            previous_point = self._points[str(j)]
            result = self._can_move(previous_point, current_point)

            if result is False:
                return False
        return True

    def _can_move(self, previous_point, current_point):
        delta_x = current_point.x - previous_point.x
        delta_y = current_point.y - previous_point.y
        delta_x_y = delta_x + delta_y
        delta_t = current_point.t - previous_point.t

        if delta_x_y == delta_t:
            return True
        elif delta_x_y < delta_t:
            return self._is_reachable(delta_x_y, delta_t)
        elif delta_x_y > delta_t:
            return False

    def _is_reachable(self, delta_x_y, delta_t):
        for i in range(delta_t + 1):
            if (1 * i + (-1) * (delta_t - i)) == delta_x_y:
                return True
        return False


class Point(object):

    def __init__(self):
        self._x = 0
        self._y = 0
        self._t = 0

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def t(self):
        return self._t

    @t.setter
    def t(self, value):
        self._t = value


if __name__ == '__main__':
    point_count = int(input())
    points = [list(map(int, input().split(" "))) for _ in range(point_count)]
    plan = TravelingPlan()
    origin = plan.add_point(str(0))

    for i in range(0, len(points)):
        point = plan.add_point(str(i + 1))
        point.t = points[i][0]
        point.x = points[i][1]
        point.y = points[i][2]

    if plan.is_executable() is True:
        print("Yes")
    else:
        print("No")
