import random
import matplotlib.pylab as pylab
def plotMeans(numDice, numRolls, numBins, legend, color, style):
	means=[]
	for i in range(numRolls//numDice):
		vals=0
		for j in range(numDice):
			vals+=5*random.random()
		means.append(vals/float(numDice))
	pylab.hist(means, numBins, color=color, label=legend, weights=pylab.array(len(means)*[1])/len(means), hatch=style)
	return means
mean, std=plotMeans(1, 1000000, 19, '1 die', 'b', '*')
print('Mean of rolling 1 die='+str(mean)+','+'Std='+std)
pylab.title('Rolling Continuous Dice')
pylab.xlabel('Value')
pylab.ylabel('Probability')
pylab.legend()


	