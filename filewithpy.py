import sys
with open(r'C:\Users\tdwil\OneDrive\Desktop\testing.txt', 'r') as File1:
    file_stuff=File1.read()
    file_firstLine=File1.readlines(3)
    print(file_stuff)
    print(file_firstLine)
    print(File1.closed)
File2=open(r'C:\Users\tdwil\OneDrive\Desktop\testing.txt', 'w')
File2.write("this is a test")

