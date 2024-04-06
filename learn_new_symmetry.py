import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from itertools import product, combinations


def make_circle(n_points=250):
    random_pi = np.random.uniform(size=n_points, low=0., high=2*np.pi)
    z = np.exp((0.+1.j)*random_pi)
    return z

# draw_circle
def draw_exp_circle(rad, ax, col=1):
    circle = rad*make_circle()
    
    new_circle = np.exp(circle)
    
    ax.scatter(circle.real, circle.imag,  marker='.', c=f"C{col}", alpha=.15)
    
    ax.scatter(new_circle.real, new_circle.imag, marker='.', c=f"C{col}", alpha=.15)
    return new_circle

# draw sphere
def draw_unit_sphere(ax):
    u, v = np.mgrid[0:2*np.pi:50j, 0:np.pi:25j]
    x = np.cos(u)*np.sin(v)
    y = np.sin(u)*np.sin(v)
    z = np.cos(v)
    ax.plot_wireframe(x, y, z, color="r")
    return

#project from complex plane onto unit sphere
def riemann_sphere(cplx_points, ax):
    pass

if __name__ == "__main__":

    fig = plt.figure()
    gs = fig.add_gridspec(1, 2)
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.set_aspect('equal')
    ax2 = fig.add_subplot(gs[0, 1], projection='3d')
    # ax2.set_aspect('equal')
    for _, rad in enumerate(np.linspace(start=0.33, stop = 2.0, num = 10) + [1.0]):
        draw_exp_circle(rad=rad, ax=ax1, col = _)
    
    draw_unit_sphere(ax2)
    plt.show()
    plt.close()

