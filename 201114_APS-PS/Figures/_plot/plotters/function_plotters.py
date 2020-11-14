#!/usr/bin/env python3

## ----------------------------------------------------------------------------
## FUNCTION PLOTTERS
## ----------------------------------------------------------------------------

from . import _helpers as _hlp

## NUMPY
import numpy as np

## MATPLOTLIB
import matplotlib as mpl
import matplotlib.pyplot as plt
# import matplotlib.animation as animation

## TIME and TQDM
# from time import time
# from time import sleep
# from tqdm import tqdm

## OTHER
# import re
# from math import fmod
# from math import floor


################################################################################
## PLOT CURVES FOR DIFFERENT VALUES OF A PARAMETER
## INPUT: function, x_min, x_max, param_values
## PARAMETERS: ...
## RETURNS: figure
################################################################################

def plot_curves(
    function, x_min, x_max, param_values,
    node_count=100, param_name=r'p',
    figsize=(8, 5), title=r'',
    xlabel=r'', xrotation='horizontal', xlabelpad=00, xradians=False,
    ylabel=r'', yrotation='horizontal', ylabelpad=10, yradians=False,
    xtick_count=9, ytick_count=7,
    linestyle='solid', linewidth=2.5, marker='None', cycler=None,
    legend=True, legend_loc='upper right', legend_ncol=2):

    ## INPUT HANDLING
    if type(param_values) is not list: param_values = [param_values]
    x_nodes = np.linspace(x_min, x_max, node_count).tolist()

    ## INITIALIZE FIGURE
    fig, ax = _hlp.init_figure(title=title, figsize=figsize,
        xlabel=xlabel, xrotation=xrotation, xlabelpad=xlabelpad,
        ylabel=ylabel, yrotation=yrotation, ylabelpad=ylabelpad)
    if cycler:
        ax.set_prop_cycle(cycler)

    ## PLOT
    y_max = -100000
    y_min = +100000
    for p in param_values:
        evals = function(x_nodes, p)
        y_min = min(y_min, min(evals) - abs(min(evals)*0.1))
        y_max = max(y_max, max(evals) + abs(min(evals)*0.1))
        ax.plot(x_nodes, evals,
            label=f'${param_name}={p}$',
            linestyle=linestyle, linewidth=linewidth, marker=marker)

    ## TICKS
    _hlp.set_xticks(ax, x_min, x_max, xtick_count, xradians)
    _hlp.set_yticks(ax, y_min, y_max, ytick_count, yradians)

    ## LEGEND
    if legend:
        plt.legend(loc=legend_loc, ncol=legend_ncol)
    return fig


################################################################################
## FILLED CONTOUR PLOT IN 2D
## INPUT: function, x_min, x_max, y_min, y_max
## PARAMETERS: ...
## RETURNS: figure
################################################################################

def plot_contourf(
    function, x_min, x_max, y_min, y_max,
    x_node_count=100, y_node_count=100,
    figsize=(8, 5), title=r'',
    xlabel=r'', xrotation='horizontal', xlabelpad=00, xradians=False,
    ylabel=r'', yrotation='horizontal', ylabelpad=10, yradians=False,
    xtick_count=9, ytick_count=7, log_scale=False,
    cmap='viridis', levels=30):

    ## INPUT HANDLING
    x_nodes = np.linspace(x_min, x_max, x_node_count).tolist()
    y_nodes = np.linspace(y_min, y_max, y_node_count).tolist()

    ## INITIALIZE FIGURE
    fig, ax = _hlp.init_figure(title=title, figsize=figsize,
        xlabel=xlabel, xrotation=xrotation, xlabelpad=xlabelpad,
        ylabel=ylabel, yrotation=yrotation, ylabelpad=ylabelpad)

    ## PLOT
    evals = function(x_nodes, y_nodes)
    z_min = min([min(z) for z in evals])
    z_min = z_min - abs(z_min*0.1)
    z_max = max([max(z) for z in evals])
    z_max = z_max + abs(z_max*0.1)
    if log_scale:
        mappable = ax.contourf(x_nodes, y_nodes, evals, levels, cmap=cmap,
            locator=mpl.ticker.LogLocator())
    else:
        mappable = ax.contourf(x_nodes, y_nodes, evals, levels, cmap=cmap)

    ## TICKS
    _hlp.set_xticks(ax, x_min, x_max, xtick_count, xradians)
    _hlp.set_yticks(ax, y_min, y_max, ytick_count, yradians)

    ## COLORBAR
    fig.colorbar(mappable)
    return fig


################################################################################
## SURFACE PLOT IN AXONOMETRIC-3D
## INPUT: function, x_min, x_max, y_min, y_max
## PARAMETERS: ...
## RETURNS: figure
################################################################################

def plot_surface(
    function, x_min, x_max, y_min, y_max,
    x_node_count=100, y_node_count=100,
    figsize=(8, 5), view=(45, 225), title=r'',
    xlabel=r'', xrotation='horizontal', xlabelpad=10, xradians=False,
    ylabel=r'', yrotation='horizontal', ylabelpad=10, yradians=False,
    zlabel=r'', zrotation='horizontal', zlabelpad=10, zradians=False,
    xtick_count=7, ytick_count=7, ztick_count=5,
    cmap='viridis', edgecolor='none'):

    ## INPUT HANDLING
    x_nodes = np.linspace(x_min, x_max, x_node_count).tolist()
    y_nodes = np.linspace(y_min, y_max, y_node_count).tolist()

    ## INITIALIZE FIGURE
    fig, ax = _hlp.init_trifigure(title=title, view=view, figsize=figsize,
        xlabel=xlabel, xrotation=xrotation, xlabelpad=xlabelpad,
        ylabel=ylabel, yrotation=yrotation, ylabelpad=ylabelpad,
        zlabel=zlabel, zrotation=zrotation, zlabelpad=zlabelpad)

    ## PLOT
    evals = function(x_nodes, y_nodes)
    z_min = min([min(z) for z in evals])
    z_min = z_min - abs(z_min*0.1)
    z_max = max([max(z) for z in evals])
    z_max = z_max + abs(z_max*0.1)
    X, Y = np.meshgrid(x_nodes, y_nodes)
    ax.plot_surface(X, Y, np.matrix(evals),
        cmap=cmap, edgecolor=edgecolor)

    ## TICKS
    _hlp.set_xticks(ax, x_min, x_max, xtick_count, xradians)
    _hlp.set_yticks(ax, y_min, y_max, ytick_count, yradians)
    _hlp.set_zticks(ax, z_min, z_max, ztick_count, zradians)

    return fig
