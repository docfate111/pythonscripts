from copy import deepcopy as copy
lowercase=lambda s: ''.join([i.lower() for i in s]) 
#1.1 Implement an algorithm to determine if a string has all unique characters. 
def isUnique(s):
    s=lowercase(s)
    d={}
    for i in s:
        if(i in [x for x in d.keys()]):
            d[i]+=1
        else:
            d[i]=1
    for x in d.values():
        if(x>1):
            return False
    return True
# What if you can not use additional data structures?
def isUnique2(s):
    s=lowercase(s)
    sofar=""
    for i in s:
        if i in sofar:
            return False
        sofar+=i
    return True
#1.2 Write code to reverse a C-Style String. (C-String means that “abcd” is represented as
#five characters, including the null character.)
rever=lambda s: ''.join([s[i] for i in range(len(s)-1, -1, -1)])
def rev(s):
    ans=""
    for i in range(len(s)-1, -1, -1):
        ans+=s[i]
    #\0 is null character
    return "\0"+ans
'''1.3 Design an algorithm and write code to remove the duplicate characters in a string
without using any additional buffer. NOTE: One or two additional variables are fine.
An extra copy of the array is not.
FOLLOW UP
Write the test cases for this method.'''
def removeDuplicate(s):
    s=lowercase(s)
    sofar=""
    ans=""
    for i in s:
        if i not in sofar:
            ans+=i
            sofar+=i
    return ans
#1.4 Write a method to decide if two strings are anagrams or not.
def isAnagram(s1, s2):
    s1=lowercase(s1)
    s2=lowercase(s2)
    d={}
    for i in s1:
        if(i in d.keys()):
            d[i]+=1
        else:
            d[i]=1
    for i in s2:
        if(i in d.keys()):
            d[i]-=1
        else:
            return False
    for x in d.values():
        if(x!=0):
            return False
    return True
#1.5 Write a method to replace all spaces in a string with ‘%20’
def replaceSpace(s):
    #return s.replace(" ", "%20") easy way
    ans=""
    for i in s:
        if(i==' '):
            ans+="%20"
        else:
            ans+=i
    return ans
#1.6 Given an image represented by an NxN matrix, where each pixel in the image is 4
#bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
'''
    ABC         ADG
    DEF  ==>    BEH
    GHI         CFI
'''
def rotate(matrix):
    m=copy(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            m[i][j]=matrix[j][i]
    return m
#1.7 Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
#column is set to 0.
def setZero(matrix):
    m=matrix
    z=-1
    #go through each row and find that index
    for i in range(len(m)):
        if(0 in m[i]):
            #find index of 0
            z=m[i].index(0)
    #set it equal to zero
    for i in range(len(m)):
        for j in range(len(m[i])):
            if(m[i][j]==0):
                m[i]=[[0]*len(m[i])][0]
            if(j==z):
                m[i][j]=0
    return m
'''1.8 Assume you have a method isSubstring which checks if one word is a substring of
another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using
only one call to isSubstring (i.e., “waterbottle” is a rotation of “erbottlewat”).
'''
rot=lambda s: s[1:]+s[0]
def isSubstring(s1, s2):
    s1=lowercase(s1)
    s2=lowercase(s2)
    count=0
    while(count<len(s2)-1):
        s1=rot(s1)
        if(s2==s1):
            return True
        count+=1
    return False
if __name__=='__main__':
    assert isUnique2("tacolq")==True
    assert isUnique2("tacocat")==False
    assert rev("deser")=="\0resed"
    assert rev("chocolate")=="\0etalocohc"
    assert removeDuplicate("eeverything")=="evrything"
    assert removeDuplicate("dduupplliiccaatte")=="duplicate"
    assert isAnagram("hello", "ohell")==True
    assert isAnagram("amazing", "amazin")==False
    assert isAnagram("hacim", "micah")==True
    assert replaceSpace("hello worlds")=="hello%20worlds"
    assert replaceSpace("there are so many spaces")=="there%20are%20so%20many%20spaces"
    assert setZero([[0, 1, 2], [3, 4, 5], [6, 7, 8]])==[[0, 0, 0], [0, 4, 5], [0, 7, 8]]
    assert setZero([[1, 1, 2, 3], [3, 0, 5, 3], [6, 7, 8, 3]])==[[1, 0, 2, 3], [0, 0, 0, 0], [6, 0, 8, 3]]
    assert setZero([[1, 1, 2], [3, 4, 5], [6, 7, 0]])==[[1, 1, 0], [3, 4, 0], [0, 0, 0]]
    assert isSubstring("waterbottle", "erbottlewat")==True
    assert isSubstring("tca", "cat")==True
    assert isSubstring("ta", "at")==True
    assert isSubstring("ta", "tb")==False
    assert rotate([['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']])==[['A', 'D', 'G'], ['B', 'E', 'H'], ['C', 'F', 'I']]
    assert rotate([[0, 1], [1, 0]])==[[0, 1], [1, 0]]
    assert rotate([[2, 3], [3, 1]])==[[2, 3], [3, 1]]