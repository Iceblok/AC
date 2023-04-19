import numpy as np
import itertools

"""
Maak een functie die twee vectoren bij elkaar optelt. De vectoren zijn Numpy arrays.
"""


class DimensionError(Exception):
    pass


def vector_addition(u: np.ndarray, v: np.ndarray) -> np.ndarray:
    summed_arrays = u.copy()

    if len(u) != len(v):
        raise DimensionError("Vectors niet hetzelfde formaat")
    else:
        for i, item in enumerate(v):
            summed_arrays[i] += v[i]
        return summed_arrays


print(vector_addition([4, 5, 6], [0., 0., 0.]))
# print(vector_addition([4, 5, 6], [0., 0.]))



