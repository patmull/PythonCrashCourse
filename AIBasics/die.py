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
    def __init__(self, num_of_trials=1000):
        self.results = []
        self.die = Die()
        self.num_of_trials = num_of_trials

    def trials(self):

        for i in range(self.num_of_trials):
            self.results.append(self.die.roll())

    def analyze_results(self, include_graph=False):

        frequencies = []
        if not len(self.results) > 0:
            raise RuntimeError("Length of the results is 0. You need to perform the dice roll first.")
        else:
            # frequency analysis
            for dice_num in self.die.get_die_values():
                frequency = self.results.count(dice_num)
                frequencies.append(frequency)

        print(frequencies)

        if include_graph == True:
            x_values = self.die.get_die_values()
            data = [Bar(x=x_values, y=frequencies)]

            x_axis_config = {'title': 'Result'}
            y_axis_config = {'title': "Frequency"}
            layout = Layout(title=f"Die trials of {self.die.num_sides} die of {self.num_of_trials} trials.",
                            xaxis=x_axis_config, yaxis=y_axis_config)
            offline.plot({'data': data, 'layout': layout}, filename='die-trials-analyzed.html')
