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
    

#test with pandas
def test_1():
    import pandas as pd
    dataset_1 = np.random.normal(size=100, loc=2, scale=1.0)
    dataset_2 = np.random.normal(size=100, loc=5, scale=5.0)
    df = pd.DataFrame()
    df['dataset_1']=dataset_1
    df['dataset_2']=dataset_2
    fig,ax = plt.subplots()
    df.plot(kind='kde',ax=ax)
    plt.show()
    fig2,ax2 = plt.subplots()
    make_norm_kde(ax, ax2)
    plt.show()
    pass

#test with seaborn
def test_2():
    import seaborn as sns
    sns.set(color_codes=True)

    dataset_1 = np.random.normal(size=100, loc=2, scale=1.0)
    dataset_2 = np.random.normal(size=100, loc=5, scale=5.0)

    fig,ax = plt.subplots()
    sns.distplot(dataset_1, hist=False, rug=False, ax=ax)
    sns.distplot(dataset_2, hist=False, rug=False, ax=ax)
    plt.show()
    
    fig2,ax2 = plt.subplots()
    make_norm_kde(ax, ax2)
    plt.show()
    pass



if __name__ == '__main__':
    test_1()
    test_2()