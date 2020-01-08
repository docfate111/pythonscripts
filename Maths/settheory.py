#how to initialize a set:
emptySet=set()
print(emptySet)
#to initialize a set with values
nums=set([1, 2, 3, 5, 7])
print(nums)
stuff=set(["I", "love", "Python"])
nums2={1, 7, 8, 9}
print(nums2)
#adding and removing from a set:
nums.add(5)
nums.remove(5)
#or ...
nums.discard(3)
nums.pop() #to remove AND RETURN
nums.clear() #remove all values from a set
for i in nums2:
	print(i)
nums={1, 3, 4, 7, 8}
print(nums.union(nums2)) #find union between sets
print(nums.intersection(nums2))
print(nums.isdisjoint(nums2)) #returns boolean if disjoint(nothing in common)
print(nums.difference(nums2)) #nums\nums2 also:
print(nums-nums2)
print(nums.symmetric_difference(nums2)) #sym diff is everything that isnt shared between sets
#or much shorter:
nums^nums2
print(3 in nums) #checks if in a set returns boolean
print(nums.issubset(nums2)) #returns boolean
print(set("String")) #converts string to set by letter
print(nums2.issuperset(nums)) #returns boolean whether or not is superset
