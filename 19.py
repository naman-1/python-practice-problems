#Read a text file and display the number of vowels/ consonants/
#uppercase/ lowercase characters in the file.
file = open('commonFile.txt','r')
content = file.read()
content = content.split()
vowels = ('a','e','i','o','u')
consonants = ('B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z')
vowelCount = 0
consonantCount = 0
upperCount = 0
lowerCount = 0
def wordSep(word):
    return (char for char in word)
for word in content:
    sepWord = wordSep(word)
    for char in sepWord:
        if char.lower() in vowels:
            vowelCount+=1 
        elif char.islower():
            lowerCount+=1
        else:
            upperCount+=1
            consonantCount+=1
print('Total no. of vowels are:',vowelCount,'Total no. of consonants are:',consonantCount,sep='\n')
print('Total no. of lower case characters are:',lowerCount,'Total no. of upper case characters are:',upperCount,sep='\n')
file.close
