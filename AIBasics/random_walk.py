import random

from matplotlib import pyplot as plt


class RandomWalk:

    def __init__(self, num_of_points=5000):
        self.num_points = num_of_points

        # START point
        self.x_values = [0]
        self.y_values = [0]

    def walk(self):
        if len(self.x_values) > self.num_points:
            raise ValueError("Enexpected state: self.num_points smaller than self.x_values.")

        # check if we are not out of scope (and canvas)
        while len(self.x_values) < self.num_points:
            random_direction_x = self.get_random_direction()
            random_distance_x = self.get_random_distance()
            step_x = random_direction_x * random_distance_x

            random_direction_y = self.get_random_direction()
            random_distance_y = self.get_random_distance()
            step_y = random_direction_y * random_distance_y

            if step_x == 0 and step_y == 0:
                continue

            # new position:
            x_old = self.x_values[-1]  # the last value (the most recent step)
            x_new = x_old + step_x
            y_old = self.y_values[-1]  # the last value (the most recent step)
            y_new = y_old + step_y

            self.x_values.append(x_new)
            self.y_values.append(y_new)

    def get_random_direction(self, min=-1, max=1):
        return random.choice([min, max])

    def get_random_distance(self, min=0, max=4, step=1):
        return random.choice(range(min, max, step))

    def plot_walk(self):
        self.walk()

        plt.style.use('classic')
        fig, axis = plt.subplots()
        axis.scatter(self.x_values, self.y_values, s=15)
        axis.scatter(self.x_values[-1], self.y_values[-1], c='red', s=100)

        # removing the visibility of the axis, since we don't need them
        axis.get_xaxis().set_visible(False)
        axis.get_yaxis().set_visible(False)

        plt.show()
