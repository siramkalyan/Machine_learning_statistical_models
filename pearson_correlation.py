from numpy.random import seed
from numpy.random import randn
from scipy.stats import pearsonr
seed(1)
# seed is used to get the random values same for two datasets 
data1=20*randn(100)
#randn gives the the defined array of  random numbers in numpy array
data2=data1+10*randn(100)
c,p=pearsonr(data1,data2)
#c is the correlation which defines one dataset is changing with respect to nother dataset
#p is the probabilty which define the correlation type
print('correlation is %.3f '%c)
print('probabiliy is %.3f'%p)
