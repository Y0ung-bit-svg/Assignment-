# a student needs to login to a zoom class. He/she is required to provide a correct meeting ID and a pass code.
# write a python function that checks if the meeting ID provided is correct if correct go ahead and ask for the pass code,
# which you are required to check if it is correct before you admit the student in the zoom class.
# TO DO;
# Use fake meeting IDs and passcode
# 1. prompt user to provide the meeting ID,
# check if it the correct one. if yes, ask for the passcode
# if passcode is correct print the message that you have been admitted by the host. You can now participate

print("Welcome to zoom class")
def zoom():
    meeting_id = int(input("Enter meeting ID:"))
    if meeting_id == 75466679710:
        passcode = int(input("Enter meeting passcode:"))
        if passcode == 17501733:
            print("You have been admitted by the host.You can now participate.")
        else:
            print("Please enter valid passcode")


    else:
        print("Please enter valid meeting ID")


zoom()