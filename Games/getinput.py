def getlist():
    l=[]
    try:
        c=str(input("Enter color(r, g, p for red, green, and purple respectively): "))
        l.append(c)
        shading=str(input("Enter shading(f, e, s for filled, empty, striped respectively): "))
        l.append(shading)
        shape=str(input("Enter shape(o, sq, d for oval, squiggle, diamond respectively): "))
        l.append(shape)
        num=int(input("Enter how many shapes there are: "))
        l.append(num)
        return l
    except:
        print("Invalid input! ")
        return []
def get(a):
    n=[[]]*a
    for i in range(a):
        print("Enter card number ", i+1)
        b=getlist()
        n[i]=b
    return n