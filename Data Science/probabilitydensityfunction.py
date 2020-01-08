import matplotlib.pyplot as plt
import math
import random
from collections import Counter
def normal_pdf(x, mu=0, sigma=1): #normal distribution, pdf-probability density function
	sqrt_2pi=math.sqrt(2*math.pi)
	return (math.exp(-(x-mu)**2/2/sigma**2)/(sqrt_2pi*sigma))
xs=[x/10.0 for x in range(-50, 50)]
'''plt.plot(xs, [normal_pdf(x) for x in xs], '-',label='mu=0,sigma=1')
plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '--',label='mu=0,sigma=2')
plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], '-',label='mu=0,sigma=0.5')
plt.plot(xs, [normal_pdf(x, mu=-1) for x in xs], '-',label='mu=-1,sigma=1')
plt.legend()
plt.title("Various Normal pdfs")
plt.show()'''
def normal_cdf(x, mu=0, sigma=1): #cumulative distribution function
	return (1+math.erf((x-mu)/math.sqrt(2)/sigma))/2
'''plt.plot(xs, [normal_cdf(x) for x in xs], '-',label='mu=0,sigma=1')
plt.plot(xs, [normal_cdf(x, sigma=2) for x in xs], '--',label='mu=0,sigma=2')
plt.plot(xs, [normal_cdf(x, sigma=0.5) for x in xs], '-',label='mu=0,sigma=0.5')
plt.plot(xs, [normal_cdf(x, mu=-1) for x in xs], '-',label='mu=-1,sigma=1')
plt.legend(loc=4)
plt.title("Various Normal cdfs")
plt.show()'''
#find approximate inverse using binary search:
def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
	#find standard then rescale
	if mu!=0 or sigma!=1:
		return mu+sigma*inverse_normal_cdf(p, tolerance=tolerance)
	low_z=-10.0
	hi_z=10.0
	while hi_z-low_z>tolerance:
		mid_z=(low_z+hi_z)/2
		mid_p=normal_cdf(mid_z)
		if mid_p<p:
			#binary search if midpt too low search above it
			low_z=mid_z
		elif mid_p>p:
			#midpt too high search above
			hi_z=mid_z
		else:
			break
	return mid_z
def bernoulli_trial(p): #random chooses between 0 and 1
	return 1 if random.random()<p else 0
def binomial(n, p): #runs bernoulli trial n times
	return sum(bernoulli_trial(p) for _ in range(n))
def make_hist(p, n, num_pts):
	data=[binomial(n, p) for _ in range(num_pts)]
	#use a bar chart to show actual binomial samples
	histogram=Counter(data)
	plt.bar([x-0.4 for x in histogram.keys()], [v/num_pts for v in histogram.values()], 0.8, color='0.75')
	mu=p*n
	sigma=math.sqrt(n*p*(1-p))
	#use a line chart to show normal approx:
	xs=range(min(data), max(data)+1)
	ys=[normal_cdf(i+0.5, mu, sigma)-normal_cdf(i-0.5, mu, sigma) for i in xs]
	plt.plot(xs, ys)
	plt.title("Binomial distribution vs. Normal approximation")
	plt.show()
make_hist(0.4, 1000, 1000)
	