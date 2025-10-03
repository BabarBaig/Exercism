"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40  # minutes
PREPARATION_TIME   = 60  # minutes

def bake_time_remaining( elapsed_bake_time: int):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes( number_of_layers):
    """ Return the time it takes to perpare the lasagna

    :param: number_of_layers: int - Each layer takes 2 min to cook
    :return: int - Total time needed to bake Guido's gorgeous lasagna.

    Returns PREPARATION_TIME, which is the time it takes to bake Guido's gorgeous lasagna
    """
    return number_of_layers * 2

def elapsed_time_in_minutes( number_of_layers, elapsed_bake_time):
    """ Return the time since baking started

    :param: number_of_layers: int - Number of layers of pasta in the lasagna.
    :param: elapsed_bake_time: int - How much time has passed since baking started
    :return: int - Time since baking started in the oven

    Returns minutes elapsed since baking started plus 2 min * number of layers in the pasta.
    """
    return elapsed_bake_time + 2 * number_of_layers
