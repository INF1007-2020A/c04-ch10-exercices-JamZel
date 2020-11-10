#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np


# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    return np.array([])


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:


def find_closest_index(values: np.ndarray, number: float) -> int:
def montecarlo():
    approximation = 0
    dans_le_cercle = 0
    pas_ds_le_cercle = 0
    liste_x_dans = []
    liste_y_dans = []
    liste_x_pas_dedans = []
    liste_y_pas_dedans = []
    i = 0

    while i < 5000:
        i += 1
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x ** 2 + y ** 2 < 1:
            dans_le_cercle += 1
            liste_x_dans.append(x)
            liste_y_dans.append(y)
        else:
            pas_ds_le_cercle += 1
            liste_x_pas_dedans.append(x)
            liste_y_pas_dedans.append(y)


        approximation = 4 * (dans_le_cercle / (pas_ds_le_cercle + dans_le_cercle))


        plt.scatter(liste_x_dans, liste_y_dans)
        plt.scatter(liste_x_pas_dedans, liste_y_pas_dedans)

    plt.show()

    return approximation

montecarlo()

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    #print(linear_values())
    #print(find_closest_index(np.ndarray[58, 78, 12, 12], 58))
    pass
