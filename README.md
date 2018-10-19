# Machine_learning_statistical_models
1.For the pearson correlation
This is the sample model for pearson coefficient as this is used if the two data sets are considered as Gaussian distributions only then this will be set valid.Supose one data variable is increasing and another is decreasing this will be a negative correlation when bot are increasing or decreaing it wil be a positive correlation .

2notes='''Hi, in this lesson, you will discover statistical methods that may
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


