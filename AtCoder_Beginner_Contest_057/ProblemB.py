'''input
5 5
-100000000 -100000000
-100000000 100000000
100000000 -100000000
100000000 100000000
0 0
0 0
100000000 100000000
100000000 -100000000
-100000000 100000000
-100000000 -100000000

5
4
3
2
1

2 2
2 0
0 0
-1 0
1 0

2
1

3 4
10 10
-10 -10
3 3
1 2
2 3
3 5
3 5

3
1
2

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    student_count, checkpoint_count = map(int, input().split())
    student_points = [list(map(int, input().split())) for i in range(1, student_count + 1)]
    check_points = [list(map(int, input().split())) for i in range(1, checkpoint_count + 1)]

    for student_point_x, student_point_y in student_points:
        point_number = 0
        shortest_distance = float('inf')
        manhattan_distance = 0

        for i in range(len(check_points)):
            diff_x = abs(student_point_x - check_points[i][0])
            diff_y = abs(student_point_y - check_points[i][1])
            manhattan_distance = diff_x + diff_y

            if manhattan_distance < shortest_distance:
                shortest_distance = manhattan_distance
                point_number = i + 1

        print(point_number)
