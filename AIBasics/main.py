from die import Die
from random_walk import RandomWalk

if __name__ == '__main__':
    # 1. Random walk
    # rand_walk = RandomWalk()
    # rand_walk.plot_walk()

    die = Die()

    die_attempts = []
    for roll_dice in range(100):
        roll = die.roll()
        die_attempts.append(roll)

    print(die_attempts)
