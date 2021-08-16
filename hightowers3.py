# Hightower's Algorithm in Python

# point = (a, b)
# finite line = point array
# infinite line = (point, point)
# obstacles = finite line array
# ADD TYPE ANNOTATION


# Return finite line array
def convert_finite(obstacles):
    finite_obstacles = []
    for point1, point2 in obstacles:
        finite_obstacle = []
        changex = point2[0] - point1[0]
        changey = point2[1] - point1[1]
        if changex != 0:
            step = 1 if changex > 0 else -1
            for i in range(0, changex+step, step):
                finite_obstacle.append((point1[0]+i, point1[1]))
        if changey != 0:
            step = 1 if changey > 0 else -1
            for i in range(0, changey+step, step):
                finite_obstacle.append((point1[0], point1[1]+i))
        finite_obstacles.append(finite_obstacle)
    return finite_obstacles


# Return True or False
def hit_obstacle(point, obstacles):
    for obstacle in obstacles:
        if point in obstacle:
            return True
    return False


# Return infinite line array
def parallel_lines(line0, lines):
    parallel_lines = []
    for line in lines:
        if get_intersection(line0, line) == None:
            parallel_lines.append(line)
    return parallel_lines


# Return finite line
def extend_finite_line(line, limit):
    extended_line1 = []
    extended_line2 = []
    point1, point2 = line[0], line[len(line)-1]
    changex = point2[0] - point1[0]
    changey = point2[1] - point1[1]
    if changex != 0:
        if changex > 0:
            step = 1
        else:
            step = -1
            limit *= -1
        for i in range(step, limit, step):
            extended_line1.append((point1[0]-i, point1[1]))
            extended_line2.append((point2[0]+i, point2[1]))
    else:
        if changey > 0:
            step = 1
        else:
            step = -1
            limit *= -1
        for i in range(step, limit, step):
            extended_line1.append((point1[0], point1[1]-i))
            extended_line2.append((point2[0], point2[1]+i))
    return extended_line1 + line + extended_line2


# Return finite line
def get_closest_parallel_lines(point, vertical, finite_lines, limit):
    vertical_lines = []
    horizontal_lines = []
    for finite_line in finite_lines:
        if finite_line[0][0] == finite_line[1][0]:
            vertical_lines.append(finite_line)
        else:
            horizontal_lines.append(finite_line)
    lines = []
    if vertical:
        for i in range(limit):
            point1 = (point[0]+i, point[1])
            for line in finite_lines:
                if point1 in extend_finite_line(line, limit):
                    lines.append(line)
            point2 = (point[0]-i, point[1])
            for line in finite_lines:
                if point2 in extend_finite_line(line, limit):
                    lines.append(line)
    else:
        for i in range(limit):
            point1 = (point[0], point[1]+i)
            for line in finite_lines:
                if point1 in extend_finite_line(line, limit):
                    lines.append(line)
            point2 = (point[0], point[1]-i)
            for line in finite_lines:
                if point2 in extend_finite_line(line, limit):
                    lines.append(line)
    return lines


# Return a infinite line
def get_escape_line_and_point(point, obstacles, vertical, visited_escape_points, limit):
    # Condition 1: just before the line hits an obstacle
    if vertical:
        for i in range(limit):
            escape_point = (point[0], point[1]+i)
            if hit_obstacle((point[0], point[1]+i+1), obstacles):
                if escape_point in visited_escape_points:
                    break
                else:
                    return (point, (point[0], point[1]+1)), escape_point
        for i in range(limit):
            escape_point = (point[0], point[1]-i)
            if hit_obstacle((point[0], point[1]-i-1), obstacles):
                if escape_point in visited_escape_points:
                    break
                else:
                    return (point, (point[0], point[1]-1)), escape_point
    else:
        for i in range(limit):
            escape_point = (point[0]+i, point[1])
            if hit_obstacle((point[0]+i+1, point[1]), obstacles):
                if escape_point in visited_escape_points:
                    break
                else:
                    return (point, (point[0]+1, point[1])), escape_point
        for i in range(limit):
            escape_point = (point[0]-i, point[1])
            if hit_obstacle((point[0]-i-1, point[1]), obstacles):
                if escape_point in visited_escape_points:
                    break
                else:
                    return (point, (point[0]-1, point[1])), escape_point
    # Condition 2: just passing one of the nearest parallel obstacle line segments
    closest_parallel_lines = get_closest_parallel_lines(
        point, vertical, obstacles, limit)
    if len(closest_parallel_lines) > 0:
        for closest_parallel_line in closest_parallel_lines:
            if vertical:
                if point[1] <= closest_parallel_line[0][1] and point[1] >= closest_parallel_line[len(closest_parallel_line)-1][1]:
                    escape_point1 = (point[0], closest_parallel_line[0][1] + 1)
                    escape_point2 = (
                        point[0], closest_parallel_line[len(closest_parallel_line)-1][1]-1)
                    if abs(escape_point1[1] - point[1]) <= abs(escape_point2[1] - point[1]):
                        finite_line = convert_finite([(point, escape_point1)])[0]
                        is_hit = False
                        for point in finite_line:
                            if hit_obstacle(point, obstacles):
                                is_hit = True
                                break
                        if not is_hit and escape_point1 in visited_escape_points:
                            return (point, (point[0], point[1]+1)), escape_point1
                    else:
                        finite_line = convert_finite([(point, escape_point2)])[0]
                        is_hit = False
                        for point in finite_line:
                            if hit_obstacle(point, obstacles):
                                is_hit = True
                                break
                        if not is_hit and escape_point2 in visited_escape_points:
                            return (point, (point[0], point[1]+1)), escape_point2
                elif point[1] >= closest_parallel_line[0][1] and point[1] <= closest_parallel_line[len(closest_parallel_line)-1][1]:
                    escape_point1 = (point[0], closest_parallel_line[0][1] - 1)
                    escape_point2 = (
                        point[0], closest_parallel_line[len(closest_parallel_line)-1][1]+1)
                    if abs(escape_point1[1] - point[1]) <= abs(escape_point2[1] - point[1]):
                        finite_line = convert_finite([(point, escape_point1)])[0]
                        is_hit = False
                        for point in finite_line:
                            if hit_obstacle(point, obstacles):
                                is_hit = True
                                break
                        if not is_hit and escape_point1 in visited_escape_points:
                            return (point, (point[0], point[1]+1)), escape_point1
                    else:
                        finite_line = convert_finite([(point, escape_point2)])[0]
                        is_hit = False
                        for point in finite_line:
                            if hit_obstacle(point, obstacles):
                                is_hit = True
                                break
                        if not is_hit and escape_point2 in visited_escape_points:
                                    return (point, (point[0], point[1]+1)), escape_point2
                else:
                    escape_point = None
                    max_distance = 0
                    escape_point1 = (point[0], closest_parallel_line[0][1] + 1)
                    escape_point2 = (
                        point[0], closest_parallel_line[len(closest_parallel_line)-1][1]-1)
                    escape_point3 = (point[0], closest_parallel_line[0][1] - 1)
                    escape_point4 = (
                        point[0], closest_parallel_line[len(closest_parallel_line)-1][1]+1)
                    if abs(escape_point1[1] - point[1]) > max_distance:
                        escape_point = escape_point1
                        max_distance = abs(escape_point1[1] - point[1])
                    if abs(escape_point2[1] - point[1]) > max_distance:
                        escape_point = escape_point2
                        max_distance = abs(escape_point2[1] - point[1])
                    if abs(escape_point3[1] - point[1]) > max_distance:
                        escape_point = escape_point3
                        max_distance = abs(escape_point3[1] - point[1])
                    if abs(escape_point4[1] - point[1]) > max_distance:
                        escape_point = escape_point4
                        max_distance = abs(escape_point4[1] - point[1])
                    finite_line = convert_finite([(point, escape_point)])[0]
                    is_hit = False
                    for point in finite_line:
                        if hit_obstacle(point, obstacles):
                            is_hit = True
                            break
                    if not is_hit and escape_point in visited_escape_points:
                        return (point, (point[0], point[1]+1)), escape_point
            else:
                if point[0] <= closest_parallel_line[0][0] and point[0] >= closest_parallel_line[len(closest_parallel_line)-1][0]:
                    escape_point1 = (closest_parallel_line[0][0] + 1, point[1])
                    escape_point2 = (closest_parallel_line[len(
                        closest_parallel_line)-1][0]-1, point[1])
                    if abs(escape_point1[0] - point[0]) <= abs(escape_point2[0] - point[0]):
                        finite_line = convert_finite([(point, escape_point1)])[0]
                        is_hit = False
                        for point in finite_line:
                            if hit_obstacle(point, obstacles):
                                is_hit = True
                                break
                        if not is_hit and escape_point1 in visited_escape_points:
                            return (point, (point[0]+1, point[1])), escape_point1
                    else:
                        finite_line = convert_finite([(point, escape_point2)])[0]
                        is_hit = False
                        for point in finite_line:
                            if hit_obstacle(point, obstacles):
                                is_hit = True
                                break
                        if not is_hit and escape_point2 in visited_escape_points:
                            return (point, (point[0]+1, point[1])), escape_point2
                elif point[0] >= closest_parallel_line[0][0] and point[0] <= closest_parallel_line[len(closest_parallel_line)-1][0]:
                    escape_point1 = (closest_parallel_line[0][0] - 1, point[1])
                    escape_point2 = (closest_parallel_line[len(
                        closest_parallel_line)-1][0]+1, point[1])
                    if abs(escape_point1[0] - point[0]) <= abs(escape_point2[0] - point[0]):
                        finite_line = convert_finite([(point, escape_point1)])[0]
                        is_hit = False
                        for point in finite_line:
                            if hit_obstacle(point, obstacles):
                                is_hit = True
                                break
                        if not is_hit and escape_point1 in visited_escape_points:
                            return (point, (point[0]+1, point[1])), escape_point1
                    else:
                        finite_line = convert_finite([(point, escape_point2)])[0]
                        is_hit = False
                        for point in finite_line:
                            if hit_obstacle(point, obstacles):
                                is_hit = True
                                break
                        if not is_hit and escape_point2 in visited_escape_points:
                            return (point, (point[0]+1, point[1])), escape_point2
                else:
                    escape_point = None
                    max_distance = 0
                    escape_point1 = (closest_parallel_line[0][0] + 1, point[1])
                    escape_point2 = (closest_parallel_line[len(
                        closest_parallel_line)-1][0]-1, point[1])
                    escape_point3 = (closest_parallel_line[0][0] - 1, point[1])
                    escape_point4 = (closest_parallel_line[len(
                        closest_parallel_line)-1][0]+1, point[1])
                    if abs(escape_point1[0] - point[0]) > max_distance:
                        escape_point = escape_point1
                        max_distance = abs(escape_point1[0] - point[0])
                    if abs(escape_point2[0] - point[0]) > max_distance:
                        escape_point = escape_point2
                        max_distance = abs(escape_point2[0] - point[0])
                    if abs(escape_point3[0] - point[0]) > max_distance:
                        escape_point = escape_point3
                        max_distance = abs(escape_point3[0] - point[0])
                    if abs(escape_point4[0] - point[0]) > max_distance:
                        escape_point = escape_point4
                        max_distance = abs(escape_point4[0] - point[0])
                    finite_line = convert_finite([(point, escape_point)])[0]
                    is_hit = False
                    for point in finite_line:
                        if hit_obstacle(point, obstacles):
                            is_hit = True
                            break
                    if not is_hit and escape_point in visited_escape_points:
                        return (point, (point[0]+1, point[1])), escape_point
    # Condition 3: no escape point
    if vertical:
        return (point, (point[0], point[1]+1)), None
    else:
        return (point, (point[0]+1, point[1])), None


# Return a point or None
def get_intersection(line1, line2):
    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])
    div = det(xdiff, ydiff)
    if div == 0:
        return None
    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return (int(x), int(y))


# Return True(there are obstacles in the way) or False
def check_obstacles(intersection, line1, line2, obstacles):
    finite_lines = convert_finite(
        [(line1[0], intersection), (line2[0], intersection)])
    for line in finite_lines:
        for point in line:
            if hit_obstacle(point, obstacles):
                return True
    return False


def hightowers(source, target, obstacles, limit: int):
    path = []

    obstacles = convert_finite(obstacles)

    visited_escape_points = [source, target]

    point1, point2 = source, target

    vertical = True
    for _ in range(100):  # tries 100 times
        line1, escape_point1 = get_escape_line_and_point(
            point1, obstacles, vertical, visited_escape_points, limit)
        vertical = not vertical
        line2, _ = get_escape_line_and_point(
            point2, obstacles, vertical, visited_escape_points, limit)
        intersection = get_intersection(line1, line2)
        if intersection != None:
            if not check_obstacles(intersection, line1, line2, obstacles):
                path.append((point1, intersection))
                path.append((intersection, point2))
                return path
            else:
                if escape_point1 != None:
                    path.append((point1, escape_point1))
                    visited_escape_points.append(escape_point1)
                    point1 = escape_point1
        else:
            raise ValueError('two lines are parallel')

    return None


# # PLAYGROUND
# print('PLAYGROUND:')
# obstacles = [((1, 0), (1, 4)), ((1, 4), (4, 4)), ((4, 4), (4, 1))]
# print(get_closest_parallel_lines((7, 2), True, convert_finite(obstacles), 10))


# # TEST 1
# print('TEST 1:')
# source = (0, 0)
# target = (0, 1)
# obstacles = []
# print('expected:', [((0, 0), (0, 1))])
# print('actual:  ', hightowers(source, target, obstacles, 10))


# # TEST 2
# print('TEST 2:')
# source = (1, 3)
# target = (3, 1)
# obstacles = [((0, 0), (0, 4)), ((
#     0, 4), (4, 4)), ((4, 4), (4, 0)), ((4, 0), (0, 0))]
# print('expected:', [((1, 3), (1, 1)), ((1, 1), (3, 1))])
# print('actual:  ', hightowers(source, target, obstacles, 10))


# TEST 3
print('TEST 3:')
source = (0, 4)
target = (3, 3)
obstacles = [((1, 0), (1, 4)), ((1, 4), (4, 4)), ((4, 4), (4, 1))]
print('expected:', [((0, 4), (0, 5)), ((0, 5), (5, 5)), ((5, 5), (5, 0)), ((5, 0), (3, 0)), ((3, 0), (3, 3))])
print('actual:  ', hightowers(source, target, obstacles, 10))


# # TEST 4
# print('TEST 4:')
# source = (0, 4)
# target = (3, 3)
# obstacles = [((1, -1), (1, 4)), ((1, 4), (4, 4)), ((4, 4), (4, 1)), ((-1, 0), (1, 0)),
#              ((-1, 0), (-1, 6)), ((-1, 6), (6, 6)), ((6, 6), (6, -1)), ((6, -1), (1, -1))]
# print('expected:', [((0, 4), (0, 5)), ((0, 5), (5, 5)), ((5, 5), (5, 0)), ((5, 0), (3, 0)), ((3, 0), (3, 3))])
# print('actual:  ', hightowers(source, target, obstacles, 10))


# # TEST 5
# print('TEST 5:')
# source = (0, 0)
# target = (2, 1)
# obstacles = [((1, 0), (1, 2)), ((1, 2), (3, 2)), ((3, 2), (3, 0)), ((3, 0), (1, 0))]
# print('expected:', None)
# print('actual:  ', hightowers(source, target, obstacles, 10))


# # TEST 6
# print('TEST 6:')
# source = (0, 0)
# target = (4, 0)
# obstacles = [((1, 0), (1, 4)), ((3, 3), (3, -5))]
# print('expected: [((0, 0), (0, -1)), ((0, -1), (2, -1)), ((2, -1), (2, 4)), ((2, 4), (4, 4)), ((4, 4), (4, 0))]')
# print('actual:  ', hightowers(source, target, obstacles, 10))


# # TEST 7
# print('TEST 7:')
# source = (0, 0)
# target = (12, 12)
# obstacles = [((1, 0), (2, 0)), ((2, 0), (2, 4)), ((0, 6), (4, 6)), ((6, 0), (6, 9)), ((
#     1, 11), (8, 11)), ((8, 5), (12, 5)), ((9, 8), (11, 8)), ((11, 8), (11, 12))]
# print('expected: [((0, 0), (0, 5)), ((0, 5), (5, 5)), ((5, 5), (5, 10)), ((5, 10), (10, 10)), ((10, 10), (10, 9)), ((10, 9), (7, 9)), ((7, 9), (7, 10)), ((7, 10), (9, 10)), ((9, 10), (9, 9)), ((9, 9), (8, 9)), ((8, 9), (8, 10)), ((8, 10), (8, 6)), ((8, 6), (12, 6)), ((12, 6), (12, 12))]')
# print('actual:  ', hightowers(source, target, obstacles, 15))


# # TEST 8
# print('TEST 8:')
# source = (1, 1)
# target = (7, 7)
# obstacles = [((0, 0), (0, 8)), ((0, 8), (8, 8)), ((8, 8), (8, 0)), ((8, 0), (0, 0)), ((
#     2, 0), (2, 5)), ((2, 5), (4, 5)), ((2, 8), (2, 7)), ((2, 7), (4, 7)), ((4, 2), (6, 2)), ((6, 2), (6, 8))]
# print('expected: [((1, 1), (1, 7)), ((1, 7), (1, 6)), ((1, 6), (5, 6)), ((5, 6), (5, 7)), ((5, 7), (5, 3)), ((5, 3), (3, 3)), ((3, 3), (3, 1)), ((3, 1), (7, 1), ((7, 1)), (7, 7))]')
# print('actual:  ', hightowers(source, target, obstacles, 15))
