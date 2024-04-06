import numpy as np
import matplotlib.pyplot as plt

def make_point_plot_pm1():
    point = np.exp((0 + 1.j)*np.random.uniform(low = -2*np.pi, high = 2*np.pi))
    p_plus_1 = point + (1.0 + 0.j)
    p_minus_1 = point  - (1.0 + 0.j)
    rat = p_minus_1/p_plus_1


    Drawing_colored_circle = plt.Circle(( 0 , 0 ), 1, fill=False)
    fig, ax = plt.subplots(1,1, figsize = (9,9))
    ax.set_aspect('equal')
    ax.set_title(f' Point: {point}')
    ax.set_xlim((-3,3))
    ax.set_ylim((-3,3))
    ax.plot([0, point.real], [0, point.imag], 'o-')
    ax.plot([0, p_plus_1.real], [0, p_plus_1.imag], '.-')
    ax.plot([0, p_minus_1.real], [0, p_minus_1.imag], '.-')
    ax.plot([0, rat.real], [0, rat.imag], 'o-')
    ax.plot([p_plus_1.real, p_minus_1.real], [p_plus_1.imag, p_minus_1.imag], '-k')
    
    ax.add_artist( Drawing_colored_circle )
    plt.show()
    return

if __name__ == "__main__":
    make_point_plot_pm1()