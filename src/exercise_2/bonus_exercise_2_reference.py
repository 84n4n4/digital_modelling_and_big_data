# Exercise 2 - bonus.

import numpy as np


# Todo - use monte carlo method to claculate pi, see https://en.wikipedia.org/wiki/Monte_Carlo_method
#   Hint: Use numpy to generate a random numbers.
#   Hint: Easiest would be to have them between 0 and 1.
#   Hint: Two random numbers form a point in 2d.
#   Hint: Calculate the distance of each random point from the source (0,0)
#   Hint: Points that have a distance of <= 1 would lie within a circle of radius 1.
#   Hint: Points that are further away are outside of the such a circle.
#   Hint: Count how many points end up in either group. The relation of this point counts can be used to calculate pi.
def monte_carlo_pi(num_points):
    A = np.random.rand(num_points)
    B = np.random.rand(num_points)
    distance_from_origin = np.sqrt(A**2 + B**2)
    points_in_circle = np.sum(distance_from_origin <= 1)
    pi_estimate = 4 * points_in_circle / num_points
    return pi_estimate


def main():
    print(monte_carlo_pi(1000000))


if __name__ == '__main__':
    main()