# -*- coding: utf-8 -*-
"""
Created on Wed Jun 07 12:48:48 2017

@author: mtinti-x

resource:
http://seaborn.pydata.org/generated/seaborn.kdeplot.html
http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.plot.kde.html
"""

import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')
import numpy as np


#this function get a kde plot x and y values
#and crete a new kde plot normalized with the
#max values
def make_norm_kde(ax_old, ax_new):
    max_points = []
    for item in enumerate(ax_old.lines):
        line = ax_old.lines[item[0]]
        max_points.append(line.get_ydata().max())
    max_points = np.array(max_points)    
    for item in enumerate(ax_old.lines):
        line = ax_old.lines[item[0]]
        ax_new.plot(line.get_xdata(), line.get_ydata()/max_points.max() )
    ax_new.set_ylim(0, 1.1)
    

if __name__ == '__main__':
    pass