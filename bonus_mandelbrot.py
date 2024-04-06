import numpy as np
import matplotlib.pyplot as plt 

def iterate_point(z, c=(1.32141-0.124j), iters = 10, ):
    it = 0
    b = z.copy()
    while it < iters:
        
        z = z**2 + c
        it += 1 
        if (z*np.conj(z)).real < 1.0:
            break
        elif (z*np.conj(z)).real  > 4:
            break

    return c, "C" + str(it) 

def generate_random_cplx(n_points = 10):
    points_real = np.random.uniform(-2,2, n_points)
    points_cplx = np.random.uniform(-2,2, n_points)
    points = points_real + (0 + 1.j)*points_cplx
    return points

def plot_mdb(n_points=5000):
    points = generate_random_cplx(n_points=np.floor_divide(n_points,10))
    other_points = generate_random_cplx(n_points)
    fig, ax = plt.subplots(1,1,figsize = (16,16))
    reals, imags, cols = [],[],[]
    for point in points:
        for other in other_points:
            pt, col = iterate_point(z= point, c=other)
            reals.append(pt.real)
            imags.append(pt.imag)
            cols.append(col)
        
    ax.scatter( reals, imags, c=cols)
    plt.show()
    plt.close()


if __name__ == "__main__":
    plot_mdb(n_points=2500)
