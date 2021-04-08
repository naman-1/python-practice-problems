def series1():
    num=int(input('enter number: '))
    stop=int(input('n0. of elements in series: '))
    sum1=0

    for i in range (stop):
        sum1+=num**i

    print('SUM IS',sum1)

series1()
