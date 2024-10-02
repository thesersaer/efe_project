import matplotlib.pyplot as plt
import numpy as np

c = 1

class WorldArrow:
    """
    Coordinate system: absolute
    t, x, y : time, right-increasing horizontal coordinate, up-increasing vertical component
    """

    def __init__(self):
        """
        np.array _s_vector
        world vector describing basic components
        """
        self._s_vector = np.array([[0.],
                                   [0.],
                                   [0.]])

        """
        np.array _v_vector
        world speed vector, normalized, time derivative of _s_vector
        """
        self._v_vector = np.array([[0.],
                                   [0.],
                                   [0.]])

    @property
    def s_vector(self):
        return self._s_vector

    def lorentz_transform(self, vel):
        lorentz_factor = (1 - vel ** 2) ** -0.5
        lorentz_matrix = np.array([[1, -vel, 0],
                                   [-vel, 1, 0],
                                   [0, 0, 1]])
        print(lorentz_factor)
        print(lorentz_matrix)
        print(lorentz_factor * lorentz_matrix)
        return lorentz_factor * lorentz_matrix @ self._s_vector

if __name__ == '__main__':
    wa = WorldArrow()
    print(wa.v_vector)
    wa.lorentz_transform(0.5)
    print(wa.v_vector)