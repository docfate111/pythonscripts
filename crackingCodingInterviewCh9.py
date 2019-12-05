'''9.1 You are given two sorted arrays, A and B,
 has a large enough buffer at the end to hold B 
  Write a method to merge B into A in sorted order
'''
def merge(a, b):
    if(len(a)==0):
        return list(b)
    if(len(b)==0):
        return list(a)
    #print(a[0], b[0])
    if(a[0]<b[0]):
        return [a[0]]+list(merge(a[1:], b))
    if(a[0]>b[0]):
        return [b[0]]+list(merge(a, b[1:]))
'''9 2 Write a method to sort an array of strings so that all 
the anagrams are next to each other
'''
def sortAnagrams(arrstr):
    q=[]
    for i in arrstr:
        q.append(''.join(sorted(i)))
    return sorted(q)
rotate=lambda s: s[1:]+[s[0]]
'''
9.3 Given  a  sorted  array  of  n  integers  that  has  been  rotated  an  unknown  number  of times, 
give an O(log n) algorithm that finds an element in the array   
You may assume that the array was originally sorted in increasing order
EXAMPLE:Input: find 5 in array (15 16 19 20 25 1 3 4 5 7 10 14)
Output: 8 (the index of 5 in the array)
'''
def findElem(e, p):
    count=0
    while(p[0]>p[-1]):
        p=rotate(p)
        count+=1
    return (count+binarySearch(p, e))%len(p)
def binarySearch(p, n):
    #n is what we are looking for inside array p
    start=0
    end=len(p)-1
    ave=(len(p)-1)//2
    while(p[ave]!=n):
        ave=(start+end+1)//2
        if(n<p[ave]):
            end=ave
        if(n>p[ave]):
            start=ave
    return ave
'''
9.5 Given a sorted array of strings which is interspersed with empty strings, write a method to find the location of a given string
Example:  find  “ball”  in  [“at”,  “”,  “”,  “”,  “ball”,  “”,  “”,  “car”,  “”,  “”,  “dad”,  “”,  “”]   4
Example: find “ballcar” in [“at”, “”, “”, “”, “”, “ball”, “car”, “”, “”, “dad”, “”, “”] will return -1
'''
def indexOf(p, n):
    d={}
    for i in range(len(p)):
        if(p[i]!=""):
            d[p[i]]=i
    #binary search
    p.remove("")
    for i in p:
        if(i==n):
            if(i in d.keys()):
                return d[i]
    return -1
    #if s in n:
    #    return s.index(n) easy way
    #return -1
cmp=lambda a, b: (a > b) - (a < b)
def strBinarySearch(p, n):
    start=0
    end=len(p)-1
    ave=end//2
    while(cmp(n, p[int(ave)])!=0):
        if(cmp(n, p[int(ave)])<0):
            end=ave
        if(cmp(n, p[int(ave)])>0):
            start=ave
        ave=(start+end)/2
    return int(ave)
'''
9 6 Given a matrix in which each row and each column is sorted, write a method to find an element in it
'''
def binarySearch2d(p, n):
    s=[]
    for i in p:
        s.extend(i)
    return binarySearch(s, n)
'''
9.7 A circus is designing a tower routine consisting of people standing atop one anoth-er’s shoulders  
For practical and aesthetic reasons, each person must be both shorter and lighter than the person below him or her  
Given the heights and weights of each person in the circus, write a method to compute the largest possible number of peo-ple in such a tower
EXAMPLE:Input (ht, wt): (65, 100) (70, 150) (56, 90) (75, 190) (60, 95) (68, 110)Output:  The  longest  tower  is  length  6  and  includes  
from  top  to  bottom:  (56,  90) (60,95) (65,100) (68,110) (70,150) (75,190)
'''
def sortTuples(s):
    l=[]
    while(len(s)!=0):
        l.append(min(s))
        s.remove(min(s))
    return l
if __name__=='__main__':
    assert merge([1, 3, 5], [2, 4, 6])==[1, 2, 3, 4, 5, 6]
    assert merge([0, 3, 4], [1, 2])==[0, 1, 2, 3, 4]
    assert merge([2], [0, 1, 5, 6, 7])==[0, 1, 2, 5, 6, 7]
    assert sortAnagrams(['hacim', 'at', 'micha', 'ta'])==['achim', 'achim', 'at', 'at']
    assert sortAnagrams(['cat', 'dgo', 'tac', 'd', 'gdo'])==['act', 'act', 'd', 'dgo', 'dgo']
    assert findElem(5, [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14])==8 
    assert findElem(6, [5, 6, 8, 9, 1, 3, 4])==1
    assert indexOf(['at',  '',  '',  '',  'ball',  '',  '',  'car',  '',  '',  'dad',  '', ''], 'ball')==4
    assert indexOf(['at', '', '', '', '', 'ball', 'car', '', '', 'dad', '', ''], 'ballcar')==-1
    assert binarySearch2d([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 7)==6
    assert sortTuples([(65, 100), (70, 150), (56, 90), (75, 190), (60, 95), (68, 110)])==[(56,  90), (60,95), (65,100), (68,110), (70,150), (75,190)]