"""
The purpose of this file is to define what the menu will look like for the tee time reservation system.
"""

import member

memberDatabase = []


def teeTimes():
    print("6:00 AM")
    print("7:00AM")
    print("8:00AM")


def menu():
    # Print the welcome menu
    print("Welcome to the Tee Time Reservation System!")
    print("Please choose from the following options.")
    print("1. Make a tee time")
    print("2. Add a new member")
    print("3. View all members")
    print("4. Exit")

    # take in user input and convert it to an integer
    choice = input()
    choice = int(choice)

    # ensure number is valid
    while choice < 1 or choice > 4:
        print("Please enter a valid number")
        choice = input()
        choice = int(choice)

    if choice == 1:
        teeTimes()
    elif choice == 2:
        # create a member object
        currMember = member.Member(None, None, None, None)
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

    elif choice == 3:
        print(memberDatabase)
