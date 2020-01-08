from itertools import combinations
from getinput import *
abbrev={'r':'red', 'g':'green', 'p':'purple', 'f':'filled', 'e':'empty', 's':'shading', 'o':'oval', 'sq':'squiggle', 'd':'diamond'}
#color, filling, shape, number
color={'r':1, 'g':2, 'p':3}
#       red, green, purple
shading={'f':1, 'e':2, 's':3}
#       filled, empty, shading
shape={'o':1, 'sq':2, 'd':3}
#       oval , squiggle, diamond
def convertToInt(ll):
    table=[]
    for l in ll:
        o=[]
        o.append(color[l[0]])
        o.append(shading[l[1]])
        o.append(shape[l[2]])
        o.append(l[3])
        table.append(o)
    return table
def isPair(cards_arr):
    for i in range(4):
        if((cards_arr[0][i]+cards_arr[1][i]+cards_arr[2][i])%3!=0):
            return False
    return True
if __name__=='__main__':
    n=convertToInt(get(3)) # what is on the table
    comb=list(combinations(n ,3))
    c=1
    for possibleSet in comb:
        if(isPair(possibleSet)):
            print(c," match?(es) found \n")
            c+=1
            count=0
            d=1
            for card in possibleSet:
                print("Card ",d)
                print()
                d+=1
                for k, v in color.items():
                    if(v==card[count]):
                        print("Color: ", abbrev[k])
                count+=1
                for k, v in shading.items():
                    if(v==card[count]):
                        print("Shading: ", abbrev[k])
                count+=1
                for k, v in shape.items():
                    if(v==card[count]):
                        print("Shape: ", abbrev[k])
                count+=1
                print("Number: ", card[count])
                count=0
                print()
    if c==1:
        print("No matches found")
