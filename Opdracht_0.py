import numpy as np

"""
Maak een functie die twee vectoren bij elkaar optelt. De vectoren zijn Numpy arrays.
"""


class DimensionError(Exception):
    pass


def vector_addition(u: np.ndarray, v: np.ndarray) -> np.ndarray:
    """
    Function adds up the given Vectors
    Example
    :param u: np.ndarray, [4, 5, 6]
    :param v: np.ndarray, [0.1, 01., 0.01]
    :return: summed_arrays: np.ndarray, [4.1, 6.0, 6.01]
    """
    summed_arrays = u.copy()

    if len(u) != len(v):
        raise DimensionError("Vectors niet hetzelfde formaat")
    else:
        for i, item in enumerate(v):
            summed_arrays[i] += v[i]
        return summed_arrays


print(vector_addition([4, 5, 6], [0.1, 01., 0.01]))
# print(vector_addition([4, 5, 6], [0., 0.]))



