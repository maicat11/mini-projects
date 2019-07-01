import random
from scipy.stats import binom


def get_sample_success(p_success, n_trials):
    '''
	Returns the number of sample successes in n_trials, where
	each trial has a probability of p_success
	'''
    return binom.ppf(random.random(), n_trials, p_success)
