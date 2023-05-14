import numpy as np

"""
Maak een functie die de negatieve van een vector geeft.
"""


def negative_of_vector(v: np.ndarray) -> np.ndarray:
    """
    Function returns the negative of given Vector
    Example
    :param v: np.ndarray, [4, 5, 6]
    :return: negative_vector: np.ndarray, [-4, -5, -6]
    """
    negative_vector = v.copy()

    for i, item in enumerate(negative_vector):
        negative_vector[i] = -v[i]
    return negative_vector


print(negative_of_vector([4, 5, 6]))