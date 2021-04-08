def series3():
    num=int(input('enter number: '))
    stop=int(input('no. of elements in series: '))
    sum1=num
    j=2
    for i in range (2,stop+1):
        sum1+=((-num)**i)/j
        j+=1
    print('SUM IS',sum1)

series3()
