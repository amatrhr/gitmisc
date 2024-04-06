import matplotlib.pyplot as plt
from mpmath.functions.functions import im
import numpy as np
from numpy.lib.function_base import diff

# find constant points in the 

def plot_a_b_ratio(a = 62-1.j, b = 1+16.j, constant = np.pi/2., n_points = 100000):
    ## Generate random complex variables
    real_parts = np.random.uniform(low = -5, high =5, size=n_points)
    im_parts = np.random.uniform(low = -5, high =5, size=n_points)
    
    ## calculate the ratios
    cplex = [x + y for x,y in zip(real_parts, im_parts)]
    output = [(z-a)/(z-b) for z in cplex] 
    diff_w_constant = (constant - np.array(output))
    diff_w_constant = [x.real for x in diff_w_constant*np.conjugate(diff_w_constant)]
    print(diff_w_constant)
    output_bins = np.linspace(min(diff_w_constant), max(diff_w_constant), num = 10000)
    print(output_bins)
    binned_output = np.digitize([z.real for z in output*np.conjugate(output)], output_bins)
    print(zip(output, output_bins))
    fig, ax = plt.subplots(1,1, figsize = (10,10))
    ax.set_xlim((-1,1))
    ax.set_ylim((-1,1))
    plt.plot([0,a.real], [0, a.imag], 'X-b', linewidth=2)
    plt.plot([0,b.real], [0, b.imag], 'X-b', linewidth=2)

    for _, rat in enumerate(output):
        if binned_output[(_)] < 1:
            plt.plot([0,rat.real], [0, rat.imag], '.-')
    

if __name__ == "__main__":
    plot_a_b_ratio()
    plt.show()

