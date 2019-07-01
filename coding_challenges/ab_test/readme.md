---
duration: 60
date: w8d1
tags:
maintainer: artificialsoph
title: A/B Test
---

### Pair Problem

In today's pair problem, we will be simulating drawing from a  _binomial distribution_. The binomial distribution is used to describe cases where we undergo a fixed number of trials, each trial has two possible outcomes, the probability of the outcomes does not change from trial to trial, and the trials are independent. The typical example of a binomial distribution problem is flipping a coin a fixed number of times. A less common example would be checking the number of parachutes that failed to open in a test batch at a parachute company.

For a binomial distribution problem, we normally phrase our questions as:
"If I do `N` trials, and each trial has a probability `prob` of succeeding, what is the probability I get X as a result?"
If you can answer this question, you can calculate the mean, variance, and other quantities of interest.

We have written a function for you that will make a sample. To use it, import it in your code as follows
```python
from generate_sample import get_sample_success

# to use it to generate the number of heads you would get flipping a coin 10 times
get_sample_success(0.5, 10)  # might return 4
get_sample_success(0.5, 10)  # might return 8

# to simulate counting the number of 6s you get after rolling a 1d6 15 times
get_sample_success(1/6.0, 15)  # might return 3
```

For many processes, such as testing whether parachutes open, we don't know the probability `p` beforehand. Instead, we know the data we have collected, and we need to infer the probability `p` from our data.

#### Your problem

We are trying to improve the proportion of defects we have when manufacturing Banana cell phones. We have some data on two different processes we want to try and use, which we call `process0` (our current process) and `process1` (the new process). It is expensive to switch to `process1` unless we are reasonably sure it makes a substaintial improvement in the rates. We will make a small production line at one factory, a run a batch of size `N` through both processes. We are employing you to help us scope out how large a batch `N` we need.

1) Suppose `p0 = 0.05` and `p1 = 0.03` (i.e `p1` is better), and we make 1,000 phones through each process. Simulate this 10,000 times and tell us in how many of those simulations `p0` ends up with fewer defects than `p1` (i.e. how many times out of this 10,000 simulations did we get the wrong result)?

2) Suppose `p0 = 0.05` and `p1 = 0.04` (i.e. `p1` is better, but less so) and we make 1,000 phones through each process. Simulating 10,000 times: how many simulations did `p0` end up with fewer defects than `p1`? How does this compare to the previous result?

3) Suppose `p0 = 0.05` and `p1 = 0.04` and we make 20,000 phones through each process. Simulating 10,000 times, what proportion of simulations did we end up with the wrong answer (i.e. claiming that we should stick with `p0`?)

4) We think that the differences are probably `p0 = 0.05` and `p1 = 0.048`. How many phones do we need to put in the batch to make sure the probability of making the wrong call is less than 1%?
