import numpy as np
import scipy.stats

def counts_from_sample(sample):
    return np.unique(sample, return_counts=True)[1]

def pc_population(p):
    """Calculate Simpson's index from population frequencies.

    p: array-like
        population species frequencies

    """
    return np.sum(p**2)

def pc_sample(sample, **kwargs):
    """Calculate Simpson's index from a sample.

    sample: array-like
        list of sampled individuals

    """
    return pc(counts_from_sample(sample), **kwargs)

def pc(n):
    """Estimate Simpson's index from sample counts.

    n: array-like
        sampled abundances
        n_i = number of counts of the ith species

    """
    n = np.asarray(n)
    n = n[n>0]
    N = np.sum(n)
    return np.sum(n*(n-1))/(N*(N-1))

def varpc_population(p, N):
    """Calculate variance of Simpson's index from population frequencies.

    p: array-like
        population species frequencies
    N: int
        sample size

    """
    return (4*N*(N-1)*(N-2)*np.sum(p**3)
            + 2*N*(N-1)*np.sum(p**2)
            - 2*N*(N-1)*(2*N-3)*np.sum(p**2)**2)/(N*(N-1))**2

def varpc_sample(sample, **kwargs):
    """Estimate variance of Simpson's index from a sample.

    sample: array-like
        list of sampled individuals

    method: string
        one of 'unbiased', 'plugin', 'grundmann', 'chao'

    bootnum: int
        number of bootstrap samples (if method='chao')

    """
 
    return varpc(counts_from_sample(sample), **kwargs)

def varpc(n, method='unbiased', bootnum=200, poisson_bound=False):
    """Estimate variance of Simpson's index from sample counts.

    n: array-like
        sampled abundances
        n_i = number of counts of the ith species

    method: string
        one of 'unbiased', 'plugin', 'grundmann', 'chao', 'shrinkage', 'poisson'

    bootnum: int
        number of bootstrap samples (if method='chao')

    poisson_bound : boolean
        use Poisson variance as bound (if method='unbiased')

    """
    n = np.asarray(n)
    N = np.sum(n)

    if (method == 'unbiased') or (method == 'shrinkage'):
        n = n[n>0]
        p2_hat = np.sum(n*(n-1))/(N*(N-1))
        var_poisson = 2/(N*(N-1))*p2_hat
        if method == 'poisson':
            return var_poisson
        p3_hat = np.sum(n*(n-1)*(n-2))/(N*(N-1)*(N-2))
        beta = 2*(2*N-3)/((N-2)*(N-3))
        var = (4*(N-2)/(N*(N-1))*(1+beta)*p3_hat
               - beta*p2_hat**2
               + 2/(N*(N-1))*(1+beta)*p2_hat
               )
        if method == 'shrinkage':
            triple_coincidences = np.sum(n*(n-1)*(n-2))/6
            kappa = 2.0/triple_coincidences
            w = min(1.0, kappa/(1+kappa))
            print(w, triple_coincidences)
            return w*var_poisson + (1-w)*var
        if poisson_bound and (var<var_poisson):
            return var_poisson
        return var
    elif method == 'plugin':
        p = n/N
        return varpc_population(p, N)
    elif method == 'grundmann':
        p = n/N
        return 4/N*(np.sum(p**3)-np.sum(p**2)**2)
    elif method == 'chao':
        p_hat = estimate_population_frequencies_chao(n)
        boot = np.random.multinomial(N, p_hat, size=bootnum)
        values = [pc(b) for b in boot]
        return np.var(values)
    else:
        raise NotImplementedError(f"Method {method} not implemented")
    
def estimate_population_frequencies_chao(n):
    """Estimate population frequency distribution accounting for unseen species
    following Chao et al.

    Implemented following https://doi.org/10.6084/m9.figshare.3568407.v1

    n: array-like
        sampled abundances
        n_i = number of counts of the ith species

    returns: population species frequencies including unseen species
    """

    n = np.asarray(n)
    N = np.sum(n)
    # no of singletons
    f1 = np.sum(n==1)
    # no of doubletons
    f2 = np.sum(n==2)
    # probability of an individual to belong to a missing species = 1 - sample coverage
    if f1 == 0:
        missing = 0
    elif f2 == 0:
        # add a pseudocount of 1 to f2 
        missing = f1/N * (N-1)*f1 / ((N-1)*f1 + 2)
    else:
        missing = f1/N * (N-1)*f1 / ((N-1)*f1 + 2*f2)
    # correct for overestimation of abundances of observed species in the sample
    lambda_hat = missing / np.sum(n/N * (1-n/N)**N)
    p_hat = n/N * (1-lambda_hat*(1-n/N)**N)
    # estimation of unseen species via Chao1
    if f2 == 0:
        f0_hat = (N-1)/N * f1 * (f1 - 1) / 2
    else:
        f0_hat = (N-1)/N * f1**2 / (2*f2)
    f0_hat_int = int(np.ceil(f0_hat))
    if f0_hat_int == 0:
        return p_hat/np.sum(p_hat)
    p_hat_unseen = missing/f0_hat * np.ones(f0_hat_int)
    p = np.concatenate((p_hat, p_hat_unseen))
    return p/np.sum(p)
