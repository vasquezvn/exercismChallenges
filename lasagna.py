"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
TIME_BY_LAYER = 2


def bake_time_remaining(current_minutes_in_oven):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes

    :number_of_layers: int - Number of layers that lasagna must have
    :return: int - time to prepare the lasagna (in minutes) derived from 'PREPARATION_TIME'.

    Function that takes minutes that each lasagna layer takes to be prepared
    and takes as argument time to each layer and return the preparation time in minutes
    """

    


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total number of minutes that lasagna has been baking in the oven

    :number_of_layers:int - number of lasagna layers
    :elapsed_bake_time:int - time that lasagna has been in the oven (in minutes)
    :return:int - the total number of minutes you've been cooking

    Function returns the total number of minutes you've been cooking, or the sum of your
    preparation time and the time the lasagna has already spent baking in the oven.
    """
    
    