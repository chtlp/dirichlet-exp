import matplotlib.pyplot as plt
import numpy as np
import sys

if __name__ == '__main__':
    alpha = 1
    H = np.array((10, 5, 3, 5), dtype=float)
    H = H / sum(H)

    if len(sys.argv) > 1:
        alpha = float(sys.argv[1])
        
    s = np.random.dirichlet(H * alpha, 20).transpose()

    plt.barh(range(20), s[0])
    plt.barh(range(20), s[1], left=s[0], color='g')
    plt.barh(range(20), s[2], left=s[0]+s[1], color='r')
    plt.title("Lengths of Strings")
    plt.show()

