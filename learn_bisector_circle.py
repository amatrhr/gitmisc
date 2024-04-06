#learn_bisector_circle
import learn_cardioid as lc
from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

@dataclass
class ComplexSegment:
    A:complex
    B:complex
    n_points:int = 100

    def __post_init__(self):
        self.midpoint = 0.5*self.A + 0.5*self.B    
        self.segment_between = self.B - self.A

        self.k = np.linspace(-5,5, num = self.n_points)
        self.perp_points = self.midpoint + self.k*(0 + 1.j)*self.segment_between
        self.transformed_points = (self.perp_points - self.A)/ (self.perp_points - self.B)
        self.mid_length = np.absolute(self.midpoint - self.A)

    def plot(self):
        fig, ax = plt.subplots(1,2,figsize=(8,8))
        plt.grid()
        
        ax[0].plot([self.A.real, self.B.real], [self.A.imag, self.B.imag], '--')
        ax[0].annotate(s=repr(np.round(self.A,2)), xy=[self.A.real, self.A.imag], )
        ax[0].annotate(s=repr(np.round(self.B,2)), xy=[self.B.real, self.B.imag], )
        ax[0].plot(self.midpoint.real, self.midpoint.imag, 'o')

        for _, point in enumerate(self.perp_points):
            ax[0].plot(point.real, point.imag, 'x')
            w_phi1 = np.arccos(self.mid_length/np.absolute(point - self.A))*np.sign(self.k[_])
            w_point = self.transformed_points[_]
            w_check = np.exp((0+1.j)*(2*w_phi1 - np.pi))

            ax[1].plot(w_point.real, w_point.imag, 'x')
            ax[1].plot([0, w_check.real], [0,w_check.imag], '.-')

        ax[0].set_aspect('equal')
        ax[1].set_aspect('equal')
        plt.show()
        plt.close()


if __name__ == "__main__":
    A = np.random.uniform(low = -5, high = 5) + (0+1.j)*np.random.uniform(low = -5, high = 5)
    B = np.random.uniform(low = -5, high = 5) + (0+1.j)*np.random.uniform(low = -5, high = 5)
    cs = ComplexSegment(A,B,35)
    cs.plot()
