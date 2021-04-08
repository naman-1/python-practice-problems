#Count and display the number of vowels, consonants, uppercase, lowercase 
#characters in string
def string():
    vowel=['a','e','i','o','u']
    vowel_count=0
    vowel_cons=0
    upper=0
    lower=0
    string=input('enter: ')
    char=list(string)
    for i in char:
        if i in vowel or i.lower() in vowel:
            vowel_count+=1
        if i not in vowel and i.lower() not in vowel and i!=' ':
            vowel_cons+=1
        if i.isupper():
            upper+=1
        if i.islower():
            lower+=1

    print('no. of vowels are:',vowel_count)
    print('no. of consonants are:',vowel_cons)
    print('no. of upper case characters are:',upper)
    print('no. of lower case characters are:',lower)


string()                 
