'''
Date:20160411
@author: zhaozhiyong
'''

from pylab import *
from numpy import *
def plot_err_cure(data):
    n = len(data)
    x = range(n)
    plot(x, data, color='r',linewidth=3)
    plt.title('Convergence curve')
    plt.xlabel('generation')
    plt.ylabel('loss')
    show()