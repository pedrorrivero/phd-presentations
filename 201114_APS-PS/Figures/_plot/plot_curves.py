#!/usr/bin/env python3

from plotters import function_plotters as fpl
from plotters.styles import PR_STYLE

import matplotlib.pyplot as plt

from numpy import pi, sin
from cycler import cycler


################################################################################
## FUNCTIONS
################################################################################

## Model
def resolution(nodes, wl):
    if type(nodes) is not list: nodes = [nodes]
    results = [];
    for n in nodes:
        result = 0
        if wl < 1: result += sin(8*n)/8
        if wl < 2: result += sin(1*n)/1
        results.append(result)
    return results


################################################################################
## PLOTS
################################################################################

x_min = -pi
x_max = pi

## Cycler
color = [
    'tab:gray', 'tab:pink', 'tab:brown', 'tab:purple',
    'tab:red', 'tab:green', 'tab:orange', 'tab:blue']
cc = (cycler(color=color) + cycler(linestyle=['-']*len(color)))

with plt.rc_context(PR_STYLE):
    ## p-curves
    fig = fpl.plot_curves(
        resolution,
        x_min, x_max, [0,1],
        node_count=200, legend=False,
        xlabel=r'$\theta$')
    fig.savefig("low-resolution")
