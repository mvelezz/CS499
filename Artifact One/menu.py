"""
The purpose of this file is to define what the menu will look like for the tee time reservation system.
"""

import member
from collections import defaultdict

memberDatabase = []
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
    while user_choice not in userChoices:
        print("Please enter a valid option.")
        user_choice = input()
    return user_choice


def menu():
    memHolder = member.Member()
    choice = getOptions()
    teeTimes = {}
    teeTimes["6:00"] = memHolder.memberNumber
    teeTimes["7:00"] = memHolder.memberNumber
    teeTimes["8:00"] = memHolder.memberNumber
    while True:
        if choice == '1':
            for time in teeTimes:
                print(time, teeTimes[time].memberNumber)
            teeTimeChoice = input("Which tee time would you like to book?")
            print("Which member would you like to add to the tee time?")
            for membersAvailable in range(len(memberDatabase)):
                print (membersAvailable)
                print(memberDatabase[membersAvailable].memberNumber)
                print(memberDatabase[membersAvailable].firstName)
                print(memberDatabase[membersAvailable].lastName)
                print(memberDatabase[membersAvailable].memberStatus)
                print()
            memberChoice = int(input())
            memberAddingToDatabase = memberDatabase[memberChoice]
            teeTimes[teeTimeChoice] = memberAddingToDatabase
            choice = getOptions()
        elif choice == '2':
            # create a member object
            currMember = member.Member()
            memberInput = input("Please enter the member number")
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
            for i in range(len(memberDatabase)):
                print(memberDatabase[i].firstName)
            choice = getOptions()
        elif choice == '4':
            break
