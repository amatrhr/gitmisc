import numpy as np
import matplotlib.pyplot as plt


def make_circle(k, res=5000):
    angles = np.linspace(0, 2*np.pi, res)
    points = k*np.array((np.sin(angles), np.cos(angles)))
    return points

def make_ray(k):
    circle_points = make_circle(k, 25).T
    # print(circle_points)
    return np.vstack((np.vstack([np.linspace([0,0], pts) for pts
     in circle_points ]),
     np.vstack([np.linspace([0.00000,0.00000], -1*pts) for pts
     in circle_points ])))


def make_grid(n_lines, k_out):
    grid = {}
    fig, ax = plt.subplots(1,2, figsize = (9,9))
    ax[0].set_aspect('equal')
    for space in np.linspace(-k_out,k_out,n_lines):
        grid[space] = [make_circle(space), 
            make_ray(k = space)]
        ax[0].plot(grid[space][0][0], grid[space][0][1] )
        ax[0].plot(grid[space][1][:,0], grid[space][1][:,1])
        ax[1].plot(grid[space][0][0]**2+grid[space][0][1]**2, 
        grid[space][0][1]/grid[space][0][0])
        ax[1].plot(grid[space][1][:,0]**2+grid[space][1][:,1]**2, 
        grid[space][1][:,1]/grid[space][1][:,0])
    plt.show()
    return grid

def transform_shape():
    pass

def plot_transformed_grid(n_shapes):
    pass


if __name__ == "__main__":
    # jj=make_ray(k=4)
    # print(jj.shape)
    # print(jj[1])
    # plt.plot(jj[:,0], jj[:,1])
    # plt.show()
    make_grid(n_lines=25, k_out=1)
    