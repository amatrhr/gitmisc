import numpy as np
import matplotlib.pyplot as plt
def square_spiral(init = 1 + 0.j, angle = np.pi/2., epsilon = 1e-1):
    vector = init
    radius = 1
    eps = 500
    fig, ax = plt.subplots(1,1, figsize = (10,10))
    ax.set_xlim((0, 1.15))
    ax.set_ylim((0, 1.15))
    ax.set_aspect('equal')
    while eps > epsilon:
    
        vector_new = vector + (1/radius)*(0 + 1.j)**(radius)
        ax.plot([vector.real, vector_new.real], [ vector.imag, vector_new.imag], '.-')
        
        # print(vector_new)
        radius += 1
        check = vector_new - vector 
        eps = (check * np.conjugate(check)).real
        vector = vector_new
        print(vector)
    
    plt.show()
    return

if __name__ == "__main__":
    square_spiral()
