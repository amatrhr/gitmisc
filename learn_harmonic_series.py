import numpy as np

def partial_sum(m, k=None, exponent = None):
    
    if exponent != None:
        k = 2 * m**exponent
    elif k != None:
        pass
    else:
        k = 2 * m**2 

    ps1 = sum([1/j for j in range(1,m +1)])
    ps2 = sum([1/j for j in range(m+1, m+k+1)])
    estimator = np.floor(k/2) * (1/(m + np.floor(k/2)) + 1/(m + np.floor(k/2) -1))
    print(f"The first partial sum, of {m} terms, is: {ps1}")
    print(f"The additional sum, of {k} additional terms, is {ps2}")
    print(f"The lower bound on the additional sum was {estimator}")
    return


if __name__ == "__main__":
    partial_sum(10000, k = 98)