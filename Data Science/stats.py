import math
def mean(x): #x is a list
	return sum(x)/len(x)
def median(v):
	n=len(v)
	sorted_v=sorted(v)
	midpt=n//2
	if n%2==1:
		return sorted_v[midpt]
	else:
		lo=midpt-1
		hi=midpt
		return (sorted_v[lo]+sorted_v[hi])/2 #average
def quartile(x, p): #p needs to be a decimal
	p_index=int(p*len(x))
	return sorted(x)[p_index]
def mode(x):
	max=0
	num=0
	for i in x:
		count=0
		for j in x:
			if i==j:
				count+=1
		if max<count:
			max=count
			num=i
	return num
def range(x):
	return max(x)-min(x)
def de_mean(x): #deviation from mean
	return [x_i-mean(x) for x_i in x]
def var(x):
	sum=0
	for i in de_mean(x):
		sum+=(i**2)
	return sum/(len(x)-1)
def std_dev(x):
	return math.sqrt(var(x))
def iqr(x): #interquartile range
	return quartile(x, 0.75)-quartile(x, 0.25)
def covar(x, y): #covariance
	sum=0
	for i, j in zip(de_mean(x), de_mean(y)):
		sum+=i*j
	return sum/(len(x)-1)
def r(x, y): #correlation coefficient r
	if std_dev(x) and std_dev(y):
		return covar(x, y)/(std_dev(x)*std_dev(y))
	else:
		return 0 
def pdf(x): #uniform probability density distribution
	return 1 if x>=0 and x<1 else 0
def cdf(x): #cumulative probability density function
	if x<0:
		return 0
	elif x<1:
		return x
	else:
		return 1

if __name__=='__main__':
	print(median([1, 2, 4, 6, 8, 5, 4, 3]))
	print(r([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 4, 0]))