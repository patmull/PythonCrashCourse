from random import randint
from plotly.graph_objs import Bar, Layout
from plotly import offline


class Die:

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)

    def get_die_values(self):
        return list(range(1, self.num_sides + 1))


class GameOfDie:
    def __init__(self, num_of_trials=1000, main_num_sides=6, num_of_dices=1):
        self.results = []
        self.dices = []
        self.frequencies = []

        for i in range(0, num_of_dices):
            self.dices.append(Die(main_num_sides))

        self.num_of_trials = num_of_trials
        self.main_num_sides = main_num_sides

    def get_dices(self):
        return self.dices

    def trials(self):
        for i in range(self.num_of_trials):
            roll_sum = 0
            for die in self.dices:
                roll_sum += die.roll()
            self.results.append(roll_sum)

    def analyze_results(self, include_graph=False):

        # one die case
        if len(self.results) < 1:
            raise RuntimeError("Length of the results is 0. You need to perform the dice roll first.")

        if include_graph is True:
            # NOTE: original solution:
            # x_values = die.get_die_values()
            max_sum = 0
            for die in self.dices:
                max_sum += die.num_sides

            x_values = list(self.generate_range_for_max_results(max_sum))

            for value in self.generate_range_for_max_results(max_result=max_sum):
                self.append_frequency(value)

            if len(self.frequencies) < 1:
                raise ValueError("Frequencies cannot be zero!")

            data = [Bar(x=x_values, y=self.frequencies)]

            x_axis_config = {'title': 'Result'}
            y_axis_config = {'title': "Frequency"}
            layout = Layout(title=f"Die trials of {self.main_num_sides} die of {self.num_of_trials} trials.",
                            xaxis=x_axis_config, yaxis=y_axis_config)
            offline.plot({'data': data, 'layout': layout}, filename='die-trials-analyzed.html')

    def append_frequency(self, dice_num):
        frequency = self.results.count(dice_num)
        self.frequencies.append(frequency)

    def generate_range_for_max_results(self, max_result):
        return range(2, max_result+1)
