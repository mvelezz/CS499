"""
The purpose of this file is to define what the menu will look like for the tee time reservation system.
"""

import member
from pandas import DataFrame

# Get the database using the method we defined in pymongo_test_insert file
from database import get_database
dbname = get_database()
collection_name = dbname["CCmembers"]

#create a list to hold the member objects
memberDatabase = []

item_details = collection_name.find()
for item in item_details:
    memberDatabase.append(item)

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

def menu():
    # use a function call to get the user choice
    choice = getOptions()
    #createa dictionary to hold tee times
    teeTimes = {}
    memHolder = member.Member
    #Tee times will hold a string as the key and a member object as the value
    teeTimes["6:00"] = 0
    teeTimes["7:00"] = 0
    teeTimes["8:00"] = 0
    #loop forever
    while True:
        if choice == '1':
            #print current tee time information
            for time in teeTimes:
                memInfo = teeTimes[time]

                print(time, teeTimes[time])
            teeTimeChoice = input("Which tee time would you like to book?")
            print("Which member would you like to add to the tee time?")
            #print all members currently in the member list
            memberChoice = int(input())
            item_details = collection_name.find_one({"_id": int(memberChoice)})
            #add member to the tee time
            print(item_details)
            teeTimes[teeTimeChoice] = item_details.values()
            choice = getOptions()
        elif choice == '2':
            # create a member object
            currMember = member.Member()
            memberInput = input("Please enter the member number")
            #typcase as the member number is an integer
            int(memberInput)
            currMember.memberNumber = int(memberInput)
            memberInput = input("Please enter the member's first name")
            currMember.firstName = memberInput
            memberInput = input("Please enter the member's last name")
            currMember.lastName = memberInput
            memberInput = input("Please enter the member's member status")
            currMember.memberStatus = memberInput
            memberDatabase.append(currMember)
            #query for inserting a member
            member_to_insert = {
                "_id": currMember.memberNumber,
                "first_name": currMember.firstName,
                "last_name": currMember.lastName,
                "member_status": currMember.memberStatus
            }

            collection_name.insert_many([member_to_insert])
            choice = getOptions()
        elif choice == '3':
            #print all members in the list
            item_details = collection_name.find()
            for item in item_details:
                # This does not give a very readable output
                print(item)
            choice = getOptions()
            
        elif choice == '4':
            memberLookingFor = input("What is the member number you want to search for?")

            #query for the database
            item_details = collection_name.find_one({"_id" : int(memberLookingFor)})
            print(item_details)
            choice = getOptions()

        elif choice == '5':
            break
