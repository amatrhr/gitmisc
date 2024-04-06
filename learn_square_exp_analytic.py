import numpy as np 
from matplotlib.patches import Rectangle, Wedge, Circle
import matplotlib.pyplot as plt
import numpy as np


class MyRectangle:
    def __init__(self, a=1, b=1):
        self.a = a
        self.b = b 
        self.vertices = [0-1.j*b, 0+1.j*b , a - b + 0.0j, a + b + 0.0j]

    @property
    def area(self):
        return (2*self.b)*(2*self.b)
    
# draw_circle
class ExpRectangle(MyRectangle):
    def __init__(self, a, b):
        super().__init__(a, b)
        self.vertices = np.exp(self.vertices)
        self.theta0 = np.angle(self.vertices[0], deg=True)
        self.theta1 = np.angle(self.vertices[1], deg=True)
        
    
    @property
    def area(self):
        # transformed rectangle is 
        return (2*self.b)*(2*self.b)

def rectangle_area_ratios():
    pass

def rectangle_plot():
    pass

if __name__ == "__main__":

    rect = MyRectangle(0.03,0.4)
    exrect = ExpRectangle(.03,0.4)
    fig,ax = plt.subplots(1,2, sharex=False, sharey=False)
    ax[0].set_aspect('equal')
    ax[0].add_patch(Rectangle((rect.vertices[0], rect.a), 2*rect.b, 
    2*rect.b, fill=False, hatch='/'))

    ax[1].add_patch(Wedge((0,0),r=exrect.vertices[3], theta1=exrect.theta0,
    theta2=exrect.theta1,width=1))
    ax[1].set_aspect('equal')
    ax[1].set_xlim(-3,3)
    ax[1].set_ylim(-3,3)
    print(vars(exrect))
    plt.show()
    plt.close()


