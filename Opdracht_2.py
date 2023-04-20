import numpy as np

"""
Maak een functie die de scalaire vermenigvuldiging van een scalar en een vector geeft.
"""


def scalar_product(s: int, v: np.ndarray) -> np.ndarray:
    multiplied = v.copy()
    for i, item in enumerate(v):
        multiplied[i] = v[i] * s
    return multiplied


print(scalar_product(1, [2, 3]))
