#working on infinite series in cplx plane:
import numpy as np 
import matplotlib.pyplot as plt
from numpy.lib.function_base import angle

def get_quadrant(arg):
    """
    get quadrant of an angle
    """
    quadrant = "IV"
    if arg < np.pi:
        quadrant = "I"
        if arg > np.pi/2:
            quadrant = "II"
    elif arg < 3*np.pi/2:
        quadrant = "III"
    
    return quadrant 


def zpiral(z, axes, n_terms=5):
    assert z*np.conj(z) <= 1
    sum = 1 + 0.j
    axes.plot([0, sum.real], [0, sum.imag], 'x-', linewidth=2)
    for index in range(1, n_terms + 1):
        term = z**(index)
        new_sum = sum + term
        axes.plot([sum.real, new_sum.real], [sum.imag, new_sum.imag], '-')
        sum = new_sum


def plot_1_1_z(z):
    """
    z: a complex number 
    """
    assert z*np.conj(z) <= 1

    transform = 1/(1-z)
    
    angle_z = np.arctan(z.imag/z.real) 
    angle_tx = np.arctan(transform.imag/transform.real) 
    print(f"Original angle: {angle_z}")
    print(f"Negative angle: {angle_z - np.pi}")

    print(f"minus-HALF Original angle: {-1*angle_z/2}")
    print(f"pi/2 minus HALF Original angle: {np.pi/2 - angle_z/2}")
    print(f"qiv test: {-(1/2)*(angle_z + np.pi)}")

    Drawing_unit_circle = plt.Circle(( 0 , 0 ), 1, fill=False)
    Drawing_hunit_circle = plt.Circle(( 0 , 0 ), np.sqrt(2), fill=False)
    print(f"Transform angle: {angle_tx}")
    fig, ax = plt.subplots(1,1,figsize=(9,9))
    # ax.set_xlim((-2.5, 2.5))
    # ax.set_ylim((-2.5, 2.5))
    ax.set_aspect('equal')
    ax.plot([0, z.real], [0, z.imag], 'o-')
    ax.plot([0, transform.real], [0, transform.imag], '.--')
    zpiral(z, ax, 2750)
    ax.add_artist( Drawing_unit_circle )
    ax.add_artist( Drawing_hunit_circle )
    plt.show()

if __name__ == "__main__":
    arg = np.random.uniform(low = 0, high = 2*np.pi)
    print(f"Angle should be: {arg}, in Q {get_quadrant(arg)}")

    point = 0.996*np.exp((0 + 1.j)*arg)
    plot_1_1_z(point)
