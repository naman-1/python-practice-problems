def series4():
    num=int(input('enter number: '))
    stop=int(input('no. of elements in series: '))
    sum1=num
    fact=1
    for i in range(2,stop+1):
        a=(-num)**i
        fact*=fact+1
        sum1+=a/fact
    print('SUM IS',sum1)
series4()
