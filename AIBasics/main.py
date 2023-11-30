from die import Die, GameOfDie
from random_walk import RandomWalk


def run_game_of_dice():
    rounds = 10000
    # NOTICE: god. Haha! (Einstein would (not) be proud!)
    god = GameOfDie(num_of_trials=rounds, num_of_dices=2)

    # Analyzing the results
    god.trials()
    god.analyze_results(include_graph=True)


if __name__ == '__main__':
    # 1. Random walk
    # rand_walk = RandomWalk()
    # rand_walk.plot_walk()
    run_game_of_dice()
