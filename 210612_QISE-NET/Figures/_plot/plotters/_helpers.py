#!/usr/bin/env python3

## ----------------------------------------------------------------------------
## PLOT HELPERS
## ----------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt


################################################################################
## INIT FIGURE
################################################################################

def init_figure(title=r'', figsize=(8, 5),
    xlabel=r'', xrotation='horizontal', xlabelpad=0,
    ylabel=r'', yrotation='horizontal', ylabelpad=10):

    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)
    ax.set_title(title)
    ax.set_xlabel(xlabel, rotation=xrotation, labelpad=xlabelpad)
    ax.set_ylabel(ylabel, rotation=yrotation, labelpad=ylabelpad)
    return fig, ax


################################################################################
## INIT 3D FIGURE
################################################################################

def init_trifigure(title=r'', figsize=(8, 5), view=(45, 225),
    xlabel=r'', xrotation='horizontal', xlabelpad=10,
    ylabel=r'', yrotation='horizontal', ylabelpad=10,
    zlabel=r'', zrotation='horizontal', zlabelpad=10):

    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, projection='3d')
    ax.view_init(view[0], view[1])
    ax.set_title(title)
    ax.set_xlabel(xlabel, rotation=xrotation, labelpad=xlabelpad)
    ax.set_ylabel(ylabel, rotation=yrotation, labelpad=ylabelpad)
    ax.set_zlabel(zlabel, rotation=zrotation, labelpad=zlabelpad)

    return fig, ax


################################################################################
## SET XTICKS
################################################################################

def set_xticks(ax, min, max, tick_count=9, radians=False):
    if radians:
        tick_labels = ['$-\pi$', '$-\pi/2$', '0', '$\pi/2$', '$\pi$']
        tick_count = len(tick_labels)
    ax.set_xlim(min, max)
    ticks_step = (max-min)/(tick_count-1)
    ticks = np.arange(min, max + ticks_step/2, step=ticks_step)
    ticks = ticks.round(decimals=1)
    ax.set_xticks(ticks)
    if radians: ax.set_xticklabels(tick_labels)


################################################################################
## SET YTICKS
################################################################################

def set_yticks(ax, min, max, tick_count=7, radians=False):
    if radians:
        tick_labels = ['$-\pi$', '$-\pi/2$', '0', '$\pi/2$', '$\pi$']
        tick_count = len(tick_labels)
    ax.set_ylim(min, max)
    ticks_step = (max-min)/(tick_count-1)
    ticks = np.arange(min, max + ticks_step/2, step=ticks_step)
    ticks = ticks.round(decimals=1)
    ax.set_yticks(ticks)
    if radians: ax.set_yticklabels(tick_labels)

################################################################################
## SET ticks
################################################################################

def set_zticks(ax, min, max, tick_count=5, radians=False):
    if radians:
        tick_labels = ['$-\pi$', '$-\pi/2$', '0', '$\pi/2$', '$\pi$']
        tick_count = len(tick_labels)
    ax.set_zlim(min, max)
    ticks_step = (max-min)/(tick_count-1)
    ticks = np.arange(min, max + ticks_step/2, step=ticks_step)
    ticks = ticks.round(decimals=1)
    ax.set_zticks(ticks)
    if radians: ax.set_zticklabels(tick_labels)
