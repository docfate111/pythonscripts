import math
class Vector(object):
	def __init__(self, coordinates):
		try:
			if not coordinates:
				raise ValueError
			self.coordinates=tuple([float(x) for x in coordinates])
			self.dimension=len(self.coordinates)
		except ValueError:
			raise ValueError('The coordinates must be filled not empty')
		except TypeError:
			raise TypeError('The coordinates must be iterable')
	def __str__(self):
		return 'Vector: {}'.format(self.coordinates)
	def __eq__(self, v):
		return self.coordinates==v.coordinates
	def __add__(self, v):
		return Vector([x+y for x,y in zip(self.coordinates, v.coordinates)])
	def __sub__(self, v):
		return Vector([x-y for x,y in zip(self.coordinates, v.coordinates)])
	def __mult__(self, c):
		#scalar multiplication represented with *
		new_coords=[float(c)*x for x in self.coordinates]
		return Vector(new_coords)
	def magnitude(self):
		sum=float(0.0)
		for i in self.coordinates:
			sum+=i**2
		return math.sqrt(sum)
	def normalized(self):
		try:
			return self*(1.0/(self.magnitude())
		except ZeroDivisionError:
			raise Exception('Cannot divide by zero')
	def __xor__(self, v):
		#dot product represented by xor symbol ^
		return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])
	#def cross(self, v):
	def dotAngle(self, v, in_degrees="False"):
		u, v=self.normalized(), v.normalized()
		#limiting cosine so that it is in domain
		def clean_cos(cos_angle):
			return min(1,max(cos_angle,-1))
		angle_rad=math.acos(clean_cos(u**v))
		if in_degrees:
			deg_to_rad=180./math.pi
			return angle_rad*deg_to_rad
		else:
			return angle_rad		
	def isOrthogonal(self, v):
		#orthogonal perpendicular tomato tomatoe
		return abs(self^v)<1e-10
	def isParallel(self, v):
		#sometimes fails need 2 fix
		return self.dotAngle(v)==0
		#self.iszero() or v.iszero() or self.dotAngle(v)==math.pi or self.dotAngle(v)==0
	def iszero(self):
		return abs(self.magnitude())<1e-10
	#def __or__(self, other):
		#cross product symbol | return '''
	def __or__(self, basis):
		#v component parallel to u:u|v
		#must not have zero vector since normalizing by zero is dividing by zero
		u=basis.normalized()
		weight=self^u
		return u*weight
	def component_orthogonal_to(self, basis):
		#remember: basis can't be zero
		proj=self|basis
		return self-proj
	def perp(self, other): #smokeperp
		return self.times_scalar(math.sin(self.vectorproj(other).dotAngle(self)))	
if __name__=='__main__':
	v=Vector([-7.579, -7.88])
	w=Vector([22.737, 23.64])
	m=Vector([3.039, 1.879])
	n=Vector([0.825, 2.036])
	print(v.isParallel(w)) #incorrect
	print(m.vectorproj(n))
	#print(m==n)
	#print(m+n)
	#print(m-n)
	#print(m.times_scalar(4))
