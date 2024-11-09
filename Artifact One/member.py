"""
This file defines the member class. It will allow the menu to create a new member and add them to a list.
"""

class Member:
    #Contsructor whem initializing a member object
    def __init__(self, memberNumber, firstName, lastName, memberStatus):
        self.memberNumber = memberNumber
        self.firstName = firstName
        self.lastName = lastName
        self.memberStatus = memberStatus
