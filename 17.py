#Create a dictionary with the roll number, name and marks of n students in a 
#class and display the names of students who have marks above 75

def dict1():
    n=int(input('enter no. of students: '))
    for i in range(n):
        d={}
        roll_num=input('enter roll number: ')
        name=input('enter name: ')
        marks=int(input('enter marks: '))
        d['name']=name
        d['roll_number']=roll_num
        d['marks']=marks
        if d['marks']>75:
            print(d)

dict1()
