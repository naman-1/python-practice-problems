#Input a list of numbers and swap elements at the even location with the 
#elements at the odd location.
def list1():
    L1=int(input('enter no. of elements in list: '))
    L2=[]
    for i in range(L1):
        L1_element=int(input('enter element: '))
        L2.append(L1_element)
    return L2
def swap(L2):
    len1=len(L2)
    if len1%2==0:
        for i in range(0,len1,2):
            L2[i],L2[i+1]=L2[i+1],L2[i]
    else:
        for i in range(0,len1-1,2):
            L2[i],L2[i+1]=L2[i+1],L2[i]
    print(L2)

swap(list1())
