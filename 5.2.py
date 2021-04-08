def series2():
    num=int(input('enter number: '))
    stop=int(input('no. of elements in series: '))
    sum1=0

    for i in range (stop):
        sum1+=(-num)**i

    print('SUM IS',sum1)

series2()
