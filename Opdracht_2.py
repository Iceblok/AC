import numpy as np

"""
Maak een functie die de scalaire vermenigvuldiging van een scalar en een vector geeft.
"""


def scalar_product(s: int, v: np.ndarray) -> np.ndarray:
    """
    Function multiplied given Vector with given integer
    Example;
    :param s: int, 2
    :param v: np.ndarray, np.array([2, 3])
    :return: multiplied: np.ndarray, np.array([4, 6])
    """
    multiplied = v.copy()

    for i in range(v.shape[0]):
        multiplied[i] = v[i] * s

    return multiplied

print(scalar_product(1, np.array([2, 3])))
print(scalar_product(2, np.array([2, 3])))
print(np.array([4, 6]))

