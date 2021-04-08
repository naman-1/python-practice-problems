#Input two numbers and display the larger / smaller number. 

def min_max():
    a=int(input('enter first number: '))
    b=int(input('enter second number: '))

    if a>b:
        print('larger number is: ',a)
        print('smaller number is: ',b)
    else:
        print('larger number is: ',b)
        print('smaller number is: ',a)


min_max()
