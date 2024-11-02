import numpy as np

c = 1

class SpeedArrow:
    def __init__(self):
        self._v_vector = np.array([
            [1.],
            [0.],
            [0.]
        ])

    def _check_valid(self):
        mod = np.linalg.norm(self._v_vector)
        error = abs(mod - 1)
        v_t = self._v_vector[0][0]

        if error < 1E-6 and v_t > 0:
            return True
        else:
            return False

    def set_vel(self, v_x, v_y):
        """
        Sets the current velocity vector to match the input.
        """
        v_mod = (v_x ** 2 + v_y ** 2) ** 0.5
        t_mod = (1. - v_mod ** 2) ** 0.5
        self._v_vector = np.array([
            [t_mod],
            [v_x],
            [v_y]
        ])


    @property
    def get(self):
        return self._v_vector

    @property
    def mod(self):
        return np.linalg.norm(self._v_vector)


class LorentzTransformation:
    def __init__(self, v_x = 0, v_y = 0):
        self.lorentz_matrix = None
        self._velocity = (v_x, v_y)

        self.set_frame_vel(v_x, v_y)

    @property
    def velocity(self):
        return self._velocity

    def set_frame_vel(self, v_x, v_y):
        v_mod = (v_x ** 2 + v_y ** 2) ** 0.5
        b_mod = v_mod / c
        b_x = v_x / c
        b_y = v_y / c
        gamma = (1 - b_mod ** 2) ** -0.5

        self.lorentz_matrix = np.array([
            [gamma, - gamma * b_x / c, - gamma * b_y / c],
            [- gamma * b_x * c, 1 + (gamma - 1) * b_x ** 2, (gamma - 1) * b_x * b_y],
            [- gamma * b_y * c, (gamma - 1) * b_x * b_y, 1 + (gamma - 1) * b_y ** 2]
        ])

    def transpose_vector(self, s_vector):
        return self.lorentz_matrix @ s_vector


if __name__ == '__main__':
    foo = SpeedArrow()
    print(foo.get)
    foo.set_vel(0.2, 0.3)
    print(foo.get)
    print(foo._check_valid())
