import json
import math


center_x = center_y = 250
max_dist = 200
num_slices = 255
triangles = []
for i in range(num_slices):
    #center = [250.0, 250.0]
    ratio_a = i / float(num_slices)
    ratio_b = (i + 1) / float(num_slices)
    angle_a = ratio_a * math.pi * 2.
    angle_b = ratio_b * math.pi * 2.
    x_a = math.cos(angle_a) * (max_dist * (ratio_a+1.)/2.) + center_x
    y_a = math.sin(angle_a) * (max_dist * (ratio_a+1.)/2.) + center_y
    x_b = math.cos(angle_b) * (max_dist * (ratio_b+1.)/2.) + center_x
    y_b = math.sin(angle_b) * (max_dist * (ratio_b+1.)/2.) + center_y
    color_a = [int(ratio_a*255), int((1-ratio_a)*255), 0]
    triangle = {
            "points": [[center_x, center_y], [x_a, y_a], [x_b, y_b]],
            "color": color_a
            }
    triangles.append(triangle)

question = {
        "width": 500,
        "height": 500,
        "background": [0, 0, 0],
        "triangles": triangles
        }

print(json.dumps(question, sort_keys=True))





