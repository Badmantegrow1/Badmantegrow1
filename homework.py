import simple_draw as sd


def polygon(point, corner, length):
    angle = 0
    angle_corner = 15
    corner_polygon = 360 / corner
    point_polygon = point
    for _ in range(corner):
        if _ < corner:

            if _ == 0:
                angle = angle_corner
            else:
                angle += corner_polygon
            s1 = sd.get_vector(start_point=point, angle=angle, length=length)
            s1.draw()
            point = s1.end_point


start = [(100, 100, 150, 3), (100, 350, 150, 4), (350, 100, 100, 5), (350, 350, 100, 6)]

for _ in start:
    point_start = sd.get_point(_[0], _[1])
    length_start = _[2]
    corner_start = _[3]
    polygon(point_start, corner_start, length_start)

# def triangle(point, angle, length):
#     while angle < 361:
#
#         point = s1.end_point
#         angle += 120
#
#
# point0 = sd.get_point(300, 300)
# triangle(point=point0, angle=angle0, length=length0)
#
#
# def square(point, angle, length):
#     while angle < 361:
#         s1 = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
#         s1.draw()
#         point = s1.end_point
#         angle += 90
#
#
# point1 = sd.get_point(50, 150)
# square(point=point1, angle=angle0, length=100)
#
#
# def pentagon(point, angle, length):
#     while angle < 361:
#         s1 = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
#         s1.draw()
#         point = s1.end_point
#         angle += 72
#
#
# point2 = sd.get_point(250, 100)
# pentagon(point=point2, angle=angle0, length=50)
#
#
# def hexagon(point, angle, length):
#
#         s1 = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
#         s1.draw()
#         point = s1.end_point
#         angle += 60
#
#
# point3 = sd.get_point(120, 400)
# hexagon(point=point3, angle=angle0, length=80)
#
#
#

# def vector(start_vector, angle, length):
#     v = sd.get_vector(start_vector, length, angle)
#     return v.end_point
#
#
# def polygon(point, heads, length):
#     angle = 0
#     angle_start = 15
#     angle_polygon = 360 / heads
#     point_polygon = point
#     for _ in range(heads):
#         if _ == 0:
#             angle = angle_start
#         else:
#             angle += angle_polygon
#         if _ < (heads - 1):
#             end_point = vector(point, length, angle)
#         else:
#             end_point = point_polygon
#         sd.line(start_point=point, end_point=end_point, color=sd.COLOR_YELLOW, width=1)
#         point = end_point
#
#
# start_point = [(100, 100, 150, 3), (100, 350, 150, 4), (350, 100, 100, 5), (350, 350, 100, 6)]
#
# for _ in start_point:
#     point_start = sd.get_point(_[0], _[1])
#     length_start = _[2]
#     heads_start = _[3]
#     polygon(point_start, heads_start, length_start)
#
sd.pause()
