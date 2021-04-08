#Input a string and determine whether it is a palindrome or not; convert the 
#case of characters in a string. 
def palindrome():
    st=input('enter STRING: ')
    if st.isupper():
        st=st.lower()
    else:
        st=st.upper()
    st1=st[::-1]
    if st1==st:
        print(st,'is palindrome')
    else:
        print(st,'is not palindrome')

palindrome()
