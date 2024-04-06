#working on infinite series in cplx plane:
import numpy as np 
import matplotlib.pyplot as plt


def make_circle(n_points=200):
    random_pi = np.random.uniform(size=n_points, low=0., high=2*np.pi)
    z = np.exp((0.+1.j)*random_pi)
    return z

def plot_cplx(array, ax=None):
    if ax is None:
        fig, ax = plt.subplots(1,1, figsize = (9,9))
    ax.set_aspect('equal')
    ax.set_xlim((-5,5))
    ax.set_ylim((-5,5))
    for z in array:
        ax.plot([0, z.real], [0, z.imag], '.-')

def annotate_func(z, func, axis):
    annot_dict = {}
    z_theta = np.arctan2(z.imag, z.real)
    z_radius = np.sqrt(z*np.conj(z)).real
    w = func(z)
    w_theta = np.arctan2(w.imag, w.real)
    w_radius = np.sqrt(w*np.conj(w)).real
    
    annot_dict["z_theta"] = np.round(z_theta,2)
    annot_dict["z_radius"] = np.round(z_radius,2)
    annot_dict["w_theta"] = np.round(w_theta,2)
    annot_dict["w_radius"] = np.round(w_radius,2)
    axis.plot([0, w.real], [0, w.imag], '.-')
    axis.annotate(text=repr(annot_dict), xy=[w.real, w.imag])

if __name__ == "__main__":

    small_circle = make_circle(5)
    plot_cplx(small_circle)
    zsq = lambda x: np.power(x+1.0, 2)
    
    ffig, ax = plt.subplots(1,1, figsize = (11,11))
    ax.set_aspect('equal')
    ax.set_xlim((-5,5))
    ax.set_ylim((-5,5))
    ax.grid()
    plot_cplx(zsq(make_circle(500)),ax=ax)
    for pint in small_circle:
        annotate_func(pint, zsq, ax)
    
    plt.show()
    plt.close()
