"""
The purpose of this file is to define what the menu will look like for the tee time reservation system.
"""

import member

#create a list to hold the member objects
memberDatabase = []
#create a user choices list so users are limited to the available choices
userChoices = ['1', '2', '3', '4']

def getOptions():
    # Print the welcome menu
    print("Welcome to the Tee Time Reservation System!")
    print("Please choose from the following options.")
    print("1. Make a tee time")
    print("2. Add a new member")
    print("3. View all members")
    print("4. Exit")
    user_choice = input()
    #limit the user choices to only those in the menu
    while user_choice not in userChoices:
        print("Please enter a valid option.")
        user_choice = input()
    return user_choice


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
            break
