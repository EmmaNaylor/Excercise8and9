import math
from math import pi, cos, tan

#height & distance in m velocity in m/s

barrel_height = 1
distance = 0.5
degree_of_elevation = 80
initial_velocity = 44
acceleration = 9.81 ** 2



theta = degree_of_elevation * (pi/180)

y = barrel_height + distance * tan(theta) - (acceleration * distance ** 2 / (2 * (initial_velocity * cos(theta)) ** 2))

print("The height of the projectile is" + " " + str(y) + " metres.")


#
# - 9.81**2 / 2(math.cos(44)theta)**2
#
# # yo
# # x
# # tan()
#
# theta = 80 * (pi/180)
# print(theta)
# print(pi)