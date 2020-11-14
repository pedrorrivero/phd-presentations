#!/usr/bin/env python3

from plotters import function_plotters as fpl
from plotters.styles import PR_STYLE

import matplotlib.pyplot as plt

from math import exp, log, ceil
from numpy import power
from scipy.special import lambertw, gammainc, gamma


################################################################################
## FUNCTIONS
################################################################################

## Threshold
def threshold(ms, rs):
    if type(ms) is not list: ms = [ms]
    if type(rs) is not list: rs = [rs]
    results = []
    for r in rs:
        _results = []
        for m in ms:
            a = ceil(-r/log(2) * lambertw(-log(2)/m/r, -1).real)
            _results.append(a)
        results.append(_results)
    return results

## Efficiency
def efficiency(m, ps, ss):
    if type(ps) is not list: ps = [ps]
    if type(ss) is not list: ss = [ss]
    results = []
    for s in ss:
        _results = []
        for p in ps:
            if m*p/s > exp(1)*log(2):
                a = ceil(-p/s/log(2) * lambertw(-log(2)/m/(p/s), -1).real)
                E = 1/a/s/log(2) * power(m/s/log(2), p) * gamma(p+1)
                E *= gammainc(p+1, a*s*log(2)) - gammainc(p+1, s*log(2))
            else:
                E = float('nan')
            _results.append(E)
        results.append(_results)
    return results


################################################################################
## PLOTS
################################################################################

# Threshold
m_min = 1
m_max = 10
r_min = 1
r_max = 10

# Efficiency
m = 2;
p_min = 2
p_max = 10
s_min = 2
s_max = 10

with plt.rc_context(PR_STYLE):
    ## Threshold
    fig = fpl.plot_contourf(
        threshold,
        m_min, m_max, r_min, r_max,
        x_node_count=800, y_node_count=800, cmap='YlGnBu_r',
        xlabel=r'$m$', ylabel=r'$r$',
        xtick_count=10, ytick_count=10,)
    fig.savefig("threshold")

    ## Efficiency
    fig = fpl.plot_contourf(
        lambda _p, _s: efficiency(m, _p, _s),
        p_min, p_max, s_min, s_max,
        x_node_count=800, y_node_count=800, cmap='hot',
        xlabel=r'$p$', ylabel=r'$s$',
        xtick_count=9, ytick_count=9, log_scale=True)
    fig.savefig("efficiency")
