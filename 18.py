# Read a text file line by line and display each word separated by a #
file = open('commonFile.txt','r')
content = file.read()
content = content.split()
for char in content:
    print(char,'#',end='',sep='')