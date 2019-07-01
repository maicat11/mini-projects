from generate_sample import get_sample_success
import numpy as np


def generate_sample(prob, sample_size=1000, num_iterations=10000):
    """
    Returns a the number of successes in a sample of size sample_size,
    simulated for num_iterations independent samples.

    Example:
    We want to know what the distribution of 6s are after 100 rolls
    of a 6-sided die. This would generate 10000 numbers, each one is
    the simulated number of 6s from 100 rolls:
    generate_sample(1/6, sample_size=100, num_iterations=10000)
    """
    return np.array(
        [get_sample_success(prob, sample_size) for _ in range(num_iterations)])


# Case 1:
# p0 = 0.05, p1 = 0.03, N = 1000
PROCESS0 = generate_sample(0.05, 1000)
PROCESS1 = generate_sample(0.03, 1000)

print("Case 1: Number of cases where we make a mistake: ",
      sum(PROCESS0 < PROCESS1))

# Case 2:
# p0 = 0.05, p1 = 0.04, N = 1000
# reuse process 0 above
PROCESS1 = generate_sample(0.04, 1000)
print("Case 2: Number of cases where we make a mistake (outof 1000): ",
      sum(PROCESS0 < PROCESS1))

# Case 3:
# p0 = 0.05, p1 =0.04, N = 20000
PROCESS0 = generate_sample(0.05, 20000)
PROCESS1 = generate_sample(0.04, 20000)
print("Case 3: Number of cases where we make a mistake (out of 20000): ",
      sum(PROCESS0 < PROCESS1))
