# An optimal quantum sampling regression algorithm for variational eigensolving in the low qubit number regime

## Introduction
My name is Pedro Rivero, and I am PhD student at IIT, working on Quantum Computing with Argonne National Lab's Physics division. Today I am going to introduce you to a new hybrid quantum-classical variational algorithm that we have come up with and refer to as QSR, or Quantum Sampling Regression algorithm.

As many of you may know, these kind of algorithms are based on the *quantum variational principle*, the most well known of which being the so called Variational Quantum Eigensolver or VQE. Nonetheless, with all its merits, this algorithm has turned out to be quite expensive to run given the way we currently access quantum processors.

To see why this is the case, let's take a look at how it works. VQE operates by simply plugging in a quantum processor inside of a classical optimization loop in order to perform some of its most expensive operations; for instance, for evaluating the target expectation value function. **FIGURE 1**

The need to send HTTP requests over the internet for querying a quantum chipset introduces a pronounced and repeating bottleneck which greatly increases the time required to execute algorithms on actual hardware. Furthermore, the classical optimizers typically used in VQE are not particularly constrained in the amount of requests that they need to make, having to compute costly quantities (e.g. numerical derivatives) for intermediate steps: a concern that hardware providers such as IBM are already trying to mitigate on their backends.

This is a real issue that often trumps researchers looking to solve problems using said algorithm; which, at the same time, has established itself as the most promising near-term path to quantum advantage. With our novel technique we try to address this.


## Algorithm outline
QSR uses Fourier analysis to come up with a grid of samples that can later be used to reconstruct the target expectation value function classically. It works as follows: **FIGURE 2**

1. Determine the bandwidth associated to each parameter determining the quantum state of your system (i.e. ansatz); an upper bound would suffice.
2. Sample the objective function using a quantum processor. **EQUATIONS (6,7)**
3. Compute the Fourier coefficients from the samples.
4. In a classical machine, solve for the global minimum of the resulting regression function.

With this strategy, in exchange for some extra classical resources, we can significantly reduced the total amount of samples that need to be performed for solving a given optimization problem. As a matter of fact, this strategy can be proved to be optimal in terms of the number of samples it requires from the quantum processor in order to fully extract the expectation value function (i.e. *Nyquist-Shannon sampling theorem*). Furthermore, because we know which samples we will need beforehand, they can all be packed in a minimal amount of queries.

This is particularly useful for state of the art technology, where getting access to a quantum a computer is still a low-offer/high-demand commodity, as it would help mitigate the load that current quantum backends have to withstand.


## Low qubit number regime
In order to assess the potential usefulness of this method it is important to contrast its efficiency with that of regular VQE. However, because the algorithms at hand are thought to be valuable for limited quantum computational capabilities —otherwise better algorithms such as phase estimation would be available— it becomes important to analyze their non-asymptotic behavior.

From computational complexity considerations, we have develop a simple analytical model to evaluate when this algorithm is more efficient than VQE. As you can see, *n* being the minimum number of domain dimensions required to solve a given optimization problem, this model shows a range in which VQE requires a considerably larger amount samples than QSR.

Also, since fully-mirroring QSR can be thought of as an optimal exhaustive search, from these same theoretical considerations we can establish a threshold above which quantum advantage can occur: the amount of domain dimensions below which QSR is more efficient than VQE. This threshold will vary from problem to problem, depending on how complicated the optimization process turns out as depicted by complexity heuristics.

**EQUATION (13,21)** & **FIGURE 3**

With all this in mind, these are the results that the model returns for different values of the threshold, and average efficiency gains in below it. As you can see efficiency gains grow exponentially with some of the parameters in our model, and the threshold can actually get quite large: up to 100 dimensions in the domain space for the analyzed cases.

**EQUATION (21,23)** & **FIGURES 4,5**


## Applicability
Some of the applications of this new techniques are:

1. Reducing the amount of queries that need to be sent to a given quantum processor in order to carry out the optimization process.
2. *Oversampling* to attain higher precision.
3. *Undersampling* to boost performance get rid of unnecessary small-wavelength oscillations leading to burdensome local minima.
4. Low-resolution start-up supplement of VQE
5. Improve convergence by removing the stochastic nature of the quantum expectation value function, stemming out of our flawed sampling process (i.e. we have neither infinite precision nor time to calculate the exact expectation values)
6. *Proxy* to transition between simulators and real devices running VQE while analyzing global properties such as error propagation in the expectation value function.
7. Fully exploit the power of our ansatz classically, avoiding the usual exponential matrix formulation of quantum mechanics.


## Benchmarking
Finally, as benchmarking, we present the results of applying the algorithm to reproduce a former well-known work; where you can see how QSR outperforms VQE just as expected.

**FIGURE 7** & **TABLE 1**

DUMITRESCU E.F., MCCASKEY A.J., HAGEN G., JANSEN G.R. ET AL., Cloud quantum computing of an atomic nucleus. Physical Review Letters, vol. 120, no. 210501 (2018), arXiv:1801.03897.


## Final thoughts
With that, I would like to thank Zack Sullivan and Ian Cloet for their direct help in conducting this work; and I will be happy to take questions. Thanks.

QISE-NET, DOE
