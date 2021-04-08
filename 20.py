#Create a binary file with name and roll number. Search for a given roll
#number and display the name, if not found display message.
import pickle
details = open('details','wb')
userNum = int(input('enter number of users: '))
userDetails = {}
for eachUser in range(userNum):
    name = input('enter your name: ')
    rollNum = int(input('enter your roll number: '))
    userDetails[rollNum] = name
pickle.dump(userDetails,details)
details.close()
def searchingOperation():
    details = open('details','rb')
    data = pickle.load(details)
    Search = int(input('enter roll number to be searched: '))
    try:
        print('name of person is: ',userDetails[Search])
        choice = input('Do you want search another person? (y/n)')
        if choice.lower() == 'y':
            searchingOperation()
    except:
        print("user is not present in database \n try again")
        searchingOperation()        

searchingOperation()