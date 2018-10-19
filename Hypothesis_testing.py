notes='''Hi, in this lesson, you will discover statistical hypothesis tests and how to compare two samples.

Data must be interpreted in order to add meaning. We can interpret data by assuming a specific structure our outcome and use statistical methods to confirm or
reject the assumption.

The assumption is called a hypothesis and the statistical tests used for this purpose are called statistical hypothesis tests.

The assumption of a statistical test is called the null hypothesis, or hypothesis zero (H0 for short). It is often called the default assumption,

or the assumption that nothing has changed. A violation of the test's assumption is often called the first hypothesis, hypothesis one, or H1 for short.

Hypothesis 0 (H0): Assumption of the test holds and is failed to be rejected.
Hypothesis 1 (H1): Assumption of the test does not hold and is rejected at some level of significance.

We can interpret the result of a statistical hypothesis test using a p-value.

The p-value is the probability of observing the data, given the null hypothesis is true.

A large probability means that the H0 or default assumption is likely. A small value, such as below 5% (0.05)

suggests that it is not likely and that we can reject H0 in favor of H1, or that something is likely to be different (e.g. a significant result).

A widely used statistical hypothesis test is the Student's t-test for comparing the mean values from two independent samples.

The default assumption is that there is no difference between the samples, whereas a rejection of this assumption suggests some significant difference.

The test assumes that both samples were drawn from a Gaussian distribution and have the same variance.

The Student's t-test can be implemented in Python via the ttest_ind() SciPy function.
'''
from numpy.random import seed
from numpy.random import randn
from scipy.stats import ttest_ind
#seed th random number generator
seed(1)
#generate two independent samples
data1=5*randn(100)+50
data2=5*randn(100)+51
#compare samples
stat,p=ttest_ind(data1,data2)
print('statistics= %.3f,p=%.3f ' %(stat,p))
#interpret
alpha=0.05
if p>alpha:
    print('same distributions(fail to reject H0)')
else:
    print('Diferernt distributions (reject h0)')
    

