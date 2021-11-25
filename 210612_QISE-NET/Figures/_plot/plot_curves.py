#!/usr/bin/env python3

from plotters import function_plotters as fpl
from plotters.styles import PR_STYLE

import matplotlib.pyplot as plt

from math import exp, log
from numpy import power, linspace
from cycler import cycler


################################################################################
## FUNCTIONS
################################################################################

## Model
def model(nodes, m, p, r):
    if type(nodes) is not list: nodes = [nodes]
    results = [];
    for n in nodes:
        n = n*exp(1) # Change scale
        results.append(power(m*n*power(2, -1*n/r), p))
    return results


################################################################################
## PLOTS
################################################################################

x_min = 0
x_max = 8
m = 2
p = 2
r = exp(1)*log(2)

## Cycler
color = [
    'tab:gray', 'tab:pink', 'tab:brown', 'tab:purple',
    'tab:red', 'tab:green', 'tab:orange', 'tab:blue']
cc = (cycler(color=color) + cycler(linestyle=['-']*len(color)))

## Straight line at y=1
nodes = linspace(x_min, x_max, 2).tolist()
evals = [1]*len(nodes)


with plt.rc_context(PR_STYLE):
    ## p-curves
    fig = fpl.plot_curves(
        lambda _n, _p: model(_n, m, _p, r),
        x_min, x_max, [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5],
        node_count=200, param_name=r'p', cycler=cc,
        xlabel=r'$n/e$')
    ax = fig.get_axes()[0]
    ax.plot(nodes, evals,
        label='None', linestyle='--', marker='None', color='#4D4D4D')
    fig.savefig("VQE-vs-QSR_p")

    ## m-curves
    fig = fpl.plot_curves(
        lambda _n, _m: model(_n, _m, p, r),
        x_min, x_max, [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5],
        node_count=200, param_name=r'm', cycler=cc,
        xlabel=r'$n/e$')
    ax = fig.get_axes()[0]
    ax.plot(nodes, evals,
        label='None', linestyle='--', marker='None', color='#4D4D4D')
    fig.savefig("VQE-vs-QSR_m")
