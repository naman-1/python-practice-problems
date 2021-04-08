#Display the terms of a Fibonacci series.

def fibonacci():
    num=int(input('enter no. of terms to display: '))
    a=0
    b=1
   
    if num<1 :
        print('enter valid nos. of terms')
    if num==1:
        print(a)
    if num==2:
        print(a,b)
    else:
         series=[0,1]
         for i in range(num-2):
              c=a+b
              a=b
              b=c
              series.append(c)
    print(series)


fibonacci()
