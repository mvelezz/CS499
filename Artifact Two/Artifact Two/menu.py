"""
The purpose of this file is to define what the menu will look like for the tee time reservation system.
"""

import member

holder1 = member.Member()
holder1.memberNumber = 1
holder1.firstName = "John"
holder1.lastName = "Smith"
holder1.memberStatus = "Full-Golf"

holder2 = member.Member()
holder2.memberNumber = 5
holder2.firstName = "Jacob"
holder2.lastName = "Jones"
holder2.memberStatus = "Full-Golf"

holder3 = member.Member()
holder3.memberNumber = 20
holder3.firstName = "Pearl"
holder3.lastName = "Myers"
holder3.memberStatus = "Full-Golf"

holder4 = member.Member()
holder4.memberNumber = 26
holder4.firstName = "Bailey"
holder4.lastName = "Amber"
holder4.memberStatus = "Part-Golf"

#create a list to hold the member objects
memberDatabase = [holder1, holder2, holder3, holder4]
#create a user choices list so users are limited to the available choices
userChoices = ['1', '2', '3', '4', '5']

def getOptions():
    # Print the welcome menu
    print("Welcome to the Tee Time Reservation System!")
    print("Please choose from the following options.")
    print("1. Make a tee time")
    print("2. Add a new member")
    print("3. View all members")
    print("4. Member lookup")
    print("5. Exit")
    user_choice = input()
    #limit the user choices to only those in the menu
    while user_choice not in userChoices:
        print("Please enter a valid option.")
        user_choice = input()
    return user_choice


# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1
def binary_search(arr, x):
    memSearch = member.Member
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1


def menu():
    # use a function call to get the user choice
    choice = getOptions()
    #createa dictionary to hold tee times
    teeTimes = {}
    memHolder = member.Member
    #Tee times will hold a string as the key and a member object as the value
    teeTimes["6:00"] = memHolder
    teeTimes["7:00"] = memHolder
    teeTimes["8:00"] = memHolder
    #loop forever
    while True:
        if choice == '1':
            #print current tee time information
            for time in teeTimes:
                memInfo = teeTimes[time]

                print(time, memInfo.memberNumber, memInfo.firstName, memInfo.lastName)
            teeTimeChoice = input("Which tee time would you like to book?")
            print("Which member would you like to add to the tee time?")
            #print all members currently in the member list
            for membersAvailable in range(len(memberDatabase)):
                print (membersAvailable)
                print(memberDatabase[membersAvailable].memberNumber)
                print(memberDatabase[membersAvailable].firstName)
                print(memberDatabase[membersAvailable].lastName)
                print(memberDatabase[membersAvailable].memberStatus)
                print()
            memberChoice = int(input())
            memberAddingToDatabase = memberDatabase[memberChoice]
            #add member to the tee time
            teeTimes[teeTimeChoice] = memberAddingToDatabase
            choice = getOptions()
        elif choice == '2':
            # create a member object
            currMember = member.Member()
            memberInput = input("Please enter the member number")
            #typcase as the member number is an integer
            int(memberInput)
            currMember.memberNumber = memberInput
            memberInput = input("Please enter the member's first name")
            currMember.firstName = memberInput
            memberInput = input("Please enter the member's last name")
            currMember.lastName = memberInput
            memberInput = input("Please enter the member's member status")
            currMember.memberStatus = memberInput
            memberDatabase.append(currMember)
            choice = getOptions()
        elif choice == '3':
            #print all members in the list
            for i in range(len(memberDatabase)):
                print(memberDatabase[i].memberNumber, memberDatabase[i].firstName, memberDatabase[i].lastName, memberDatabase[i].memberStatus )
            choice = getOptions()
        elif choice == '4':
            # create a list to store member numbers,
            memNumbers = []
            # loop through member database to collect member numbers
            for i in memberDatabase:
                memNumbers.append(int(i.memberNumber))
            #sort the member numbers to perfrom a binary search
            memNumbers.sort()
            memberLookingFor = int(input("What is the member number you want to search for?"))
            #perform binary search and output the member information based on the member number
            memberSearchResult = binary_search(memNumbers, memberLookingFor)
            memberFinalResult = memberDatabase[memberSearchResult]
            print(memberFinalResult.firstName, memberFinalResult.lastName, memberFinalResult.memberStatus)
            choice = getOptions()

        elif choice == '5':
            break
