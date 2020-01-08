import random
import numpy as np
#generates pi using Buffon-Laplace
#circle with center at (0, 0) and radius of n so that the max x and y is +2n while min is -2n
n=1000
circlePts=0
squarePts=0
for i in range(50000000):
	xc, yc=random.randrange(-n, n), random.randrange(-n, n)
	#xc is xcoordinate defined within the bounds of the square n**2 is the radius of the circle
	if xc**2+yc**2<=n**2:
		circlePts+=1
	squarePts+=1
print("pi is equal to "+str(float(4*(circlePts)/(squarePts))))
print("add more data points to get closer results:"+str(np.pi))
