#!/usr/bin/env python3

## ----------------------------------------------------------------------------
## PLOT STYLES
## CALL: with plt.rc_context(<style>)
## PARAMETERS: print(mpl.rcParams.keys())
## ALTERNATIVES: plt.style.use('ggplot')
## ----------------------------------------------------------------------------

################################################################################
## PR STYLE
################################################################################

PR_STYLE = {
    'axes.edgecolor':'black', 'axes.grid': True,
    'axes.facecolor':'white', 'axes.labelcolor': 'black', 'axes.linewidth': 1.4,
    'figure.facecolor': (1, 1, 1, 0), 'figure.figsize': [8.0, 5.0],
    'figure.titlesize': 'large', 'font.family': 'serif', 'font.size': 22,
    'grid.color': 'lightgrey', 'legend.edgecolor': 'lightgrey',
    'legend.fontsize': 20, 'legend.facecolor': 'whitesmoke',
    'lines.linestyle': '-', 'lines.linewidth': 2, 'lines.markersize': 6.0,
    'savefig.bbox': 'tight', 'savefig.directory': '~',
    'savefig.format': 'pdf', 'savefig.orientation': 'portrait',
    'savefig.transparent': False, 'text.usetex': True,
    'xtick.color':'black', 'xtick.direction': 'out',
    'xtick.major.size': 4, 'xtick.major.width': 1.2,
    'xtick.minor.size': 2.5, 'xtick.minor.width': 1.0,
    'ytick.color':'black', 'ytick.direction': 'out',
    'ytick.major.size': 4, 'ytick.major.width': 1.2,
    'ytick.minor.size': 2.5, 'ytick.minor.width': 1.0}
