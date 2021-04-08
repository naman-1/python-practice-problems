# Create a binary file with roll number, name and marks. Input a roll
# number and update the marks.

import pickle

details = open('details','wb')
userNum = int(input('enter number of users: '))
userDetails = {}
for eachUser in range(userNum):
    name = input('enter your name: ')
    marks = int(input('Enter your marks: '))
    rollNum = int(input('enter your roll number: '))
    userDetails[rollNum] = [name,marks]
pickle.dump(userDetails,details)
details.close()

def searchingOperation():
    details = open('details','rb+') 
    userDetails = pickle.load(details)
    Search = int(input('enter roll number to be searched: '))
    try:
        print('name of person is: ',userDetails[Search][0])
        print('Are you sure you want to update marks for this person? (y/n)')
        updateChoice = input()
        if updateChoice.lower() == 'y':
            updatedMarks = int(input('enter new marks: '))
            userDetails[Search][1] = updatedMarks
            pickle.dump(userDetails,details)
            print(userDetails)
            details.close()
        choice = input('Do you want to update other person\'s marks? (y/n)')
        if choice.lower() == 'y':
            searchingOperation()
        
    except:
        print("user is not present in database\ntry again")
        searchingOperation()        
    

searchingOperation()