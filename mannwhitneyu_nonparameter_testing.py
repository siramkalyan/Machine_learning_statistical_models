notes='''Hi, in this lesson, you will discover statistical methods that may
be used when your data does not come from a Gaussian distribution.

A large portion of the field of statistics and statistical methods
is dedicated to data where the distribution is known.

Data in which the distribution is unknown or cannot be easily
identified is called nonparametric.

In the case where you are working with nonparametric data,
specialized nonparametric statistical methods can be used
that discard all information about the distribution.
As such, these methods are often referred to as distribution-free methods.

Before a nonparametric statistical method can be applied,
the data must be converted into a rank format.
As such, statistical methods that expect data in rank format are sometimes
called rank statistics, such as rank correlation
and rank statistical hypothesis tests. Ranking data is exactly as
its name suggests.

The procedure is as follows:
Sort all data in the sample in ascending order.
Assign an integer rank from 1 to N for each unique value in the data sample.
A widely used nonparametric statistical hypothesis test
for checking for a difference between two independent samples
is the Mann-Whitney U test, named for Henry Mann and Donald Whitney.

It is the nonparametric equivalent of the Student's t-test but does
not assume that the data is drawn from a Gaussian distribution.

The test can be implemented in Python via the mannwhitneyu() SciPy function.

The example below demonstrates the test on two data samples drawn from a uniform distribution known to be different.'''

from numpy.random import seed
from numpy.random import randn
from scipy.stats import mannwhitneyu
seed(1)
# generate two independent samples
data1 = 50 + (randn(100) * 10)
data2 = 51 + (randn(100) * 10)
# compare samples
stat, p = mannwhitneyu(data1, data2)
print('statiscs is %.3f and p is %.3f ' %(stat,p))
#now intrepret
alpha=0.05
if p> alpha:
    print('same distributions (failed to reject hypothesis)')
else:
    print('different distribution (failed or rejected hypothesis)')
    

