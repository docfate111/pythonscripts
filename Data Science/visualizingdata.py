from matplotlib import pyplot as plt
'''#simple line plot example:
years=[1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp=[300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
plt.title("Nominal gdp")
plt.ylabel("Billions of $")
#plt.show()
#bar chart example:
cookies=["oatmeal", "raspberry", "coconut"]
num_of_cookies=[2, 3, 8]
center bars by adding .1 to each of them
xs=[i+0.1 for i, _ in enumerate(num_of_cookies)]
plt.bar(xs, num_of_cookies)
plt.ylabel("# of cookies")
plt.title("cookie inventory")
plt.xticks([i+.5 for i, _ in enumerate(num_of_cookies)], num_of_cookies)
#plt.show()
#line chart example:
var=[1, 2, 4, 8, 16, 32, 64, 128, 256]
#var for variance
bias_squared=[256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error=[x+y for x, y in zip(var, bias_squared)]
xs=[i for i, _ in enumerate(var)]
plt.plot(xs, var, 'g-', label='var') #g- green line
plt.plot(xs, bias_squared, 'r-', label='bias^2')
plt.plot(xs, total_error, 'b-', label='total error') #blue dashed line
plt.legend(loc=9) #"location top center
plt.xlabel("model complexity")
plt.title("The bias var tradeoff")
plt.show()
'''
#scatterplot example:
songrating=[12, 34, 56, 76, 33, 99, 81, 100]
volume=[10, 23, 37, 17, 55, 78, 94, 100]
labels=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
plt.scatter(songrating, volume)
for label, songrating, volume in zip(labels, songrating, volume):
	plt.annotate(label, xy=(songrating, volume), xytext=(5, -5), textcoords='offset points') 
plt.title("Song rating vs. Volume")
plt.xlabel("volume")
plt.ylabel("song rating")
plt.show()

