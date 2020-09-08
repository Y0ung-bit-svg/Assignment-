#Task two
name = str(input("Enter your name:"))
print("Hello",name,"what is your score in the following subjects ?")
english = int(input("Enter your english score:"))
maths = int(input("Enter your maths score:"))
chemistry = int(input("Enter your chemistry score:"))
physics = int(input("Enter your physics score:"))
total_score = english + maths + chemistry + physics
mean_score = total_score/4
print("Hello",name,"your total score is",total_score,"and mean is",mean_score)
