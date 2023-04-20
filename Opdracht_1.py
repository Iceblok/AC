import numpy as np

"""
Maak een functie die de negatieve van een vector geeft.
"""


def negative_of_vector(v: np.ndarray) -> np.ndarray:
    negative_vector = v.copy()

    for i, item in enumerate(negative_vector):
        negative_vector[i] = -v[i]
    return negative_vector


print(negative_of_vector([4, 5, 6]))