

----

\subsection{\hfill{}4.c. Thompson Sampling : Bayesian index policy\hfill{}}

FIXME remove this

# Thompson Sampling : Bayesian approach
A dynamic device assumes a stochastic hypothesis on the background traffic, modeled as Bernoulli distributions.

- Rewards $r_k(\tau)$ are assumed to be *i.i.d.* samples from a Bernoulli distribution $\mathrm{Bern}(\mu_k)$.

- A **binomial Bayesian posterior** is kept on the mean availability $\mu_k$ : $\mathrm{Bin}(1 + X_k(\tau), 1 + T_k(\tau) - X_k(\tau))$.
- Starts with a *uniform prior* : $\mathrm{Bin}(1, 1) \sim \mathcal{U}([0,1])$.

1. Each step $\tau \geq 1$, draw a sample from each posterior
  $i_k(\tau) \sim \mathrm{Bin}(a_k(\tau), b_k(\tau))$,
2. Choose channel $A(\tau) = \mathop{\arg\max}\limits_k \; i_k(\tau)$,
3. Update the posterior after receiving `Ack` or if collision.


\vfill{}\hfill{}\tiny{\textcolor{gray}{References: [Thompson, 1933], [Kaufmann et al, 2012]}}