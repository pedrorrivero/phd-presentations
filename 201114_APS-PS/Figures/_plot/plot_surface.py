#!/usr/bin/env python3

from plotters import function_plotters as fpl
from plotters.styles import PR_STYLE

import matplotlib.pyplot as plt

import numpy as np
import json

################################################################################
## FUNCTIONS
################################################################################

## Regression function
def QSR_regression(theta, eta, coefficients):
    if type(theta) is not list: theta = [theta]
    if type(eta) is not list: eta = [eta]
    coef = coefficients
    results = []
    for e in eta:
        _results = []
        for t in theta:
            a = coef[0] + \
                coef[1]*np.cos(t) + coef[2]*np.cos(e) + \
                coef[3]*np.sin(t) + coef[4]*np.sin(t) + \
                coef[5]*np.cos(t)*np.cos(e) + \
                coef[6]*np.cos(t)*np.sin(e) + \
                coef[7]*np.sin(t)*np.cos(e) + \
                coef[8]*np.sin(t)*np.sin(e) + \
                coef[9]*np.cos(2*t) + coef[10]*np.cos(2*e) + \
                coef[11]*np.sin(2*t) + coef[12]*np.sin(2*e) + \
                coef[13]*np.cos(t)*np.cos(2*e) + \
                coef[14]*np.cos(t)*np.sin(2*e) + \
                coef[15]*np.cos(2*t)*np.cos(e) + \
                coef[16]*np.cos(2*t)*np.sin(e) + \
                coef[17]*np.cos(2*t)*np.cos(2*e) + \
                coef[18]*np.cos(2*t)*np.sin(2*e) + \
                coef[19]*np.sin(t)*np.cos(2*e) + \
                coef[20]*np.sin(t)*np.sin(2*e) + \
                coef[21]*np.sin(2*t)*np.cos(e) + \
                coef[22]*np.sin(2*t)*np.sin(e) + \
                coef[23]*np.sin(2*t)*np.cos(2*e) + \
                coef[24]*np.sin(2*t)*np.sin(2*e)
            _results.append(a)
        results.append(_results)
    return results


################################################################################
## PLOTS
################################################################################

pi = np.pi
t_min = -pi
t_max = pi
e_min = -pi
e_max = pi

with open('data/QSR-coefficients.json', 'r') as infile:
    coefficients = json.load(infile)

with plt.rc_context(PR_STYLE):
    ## Regression
    fig = fpl.plot_surface(
        lambda _t, _e: QSR_regression(_t, _e, coefficients),
        t_min, t_max, e_min, e_max,
        figsize=(10, 7), view=(40, 205), cmap='viridis_r',
        xlabel=r'$\theta$', ylabel=r'$\eta$', zlabel=r'$\langle H_3 \rangle$',
        xradians=True, yradians=True)
    fig.savefig("QSR")
