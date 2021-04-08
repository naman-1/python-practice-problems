#Compute the greatest common divisor and least common multiple of two 
#integers.

num1=int(input('enter first number: '))          #TAKING INPUT NUMBERS
num2=int(input('enter second number: '))

if num1>num2:                                     #COMPARE NUMBERS
    greater=num1
    smaller=num2
else:
    greater=num2
    smaller=num2

def Hcf(num1,num2,smaller):
    a=smaller//2
    for i in range(a,1,-1):
        if num1%i==0 and num2%i==0:
            print('HCF is',i)
            break
    
    
def Lcm(num1,num2,greater):
    a=greater
    while True:
        if greater%num1==0 and greater%num2==0:
            print(greater,'is LCM')
            break
        greater+=a

Hcf(num1,num2,smaller)
Lcm(num1,num2,greater)
   
