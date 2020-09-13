#write a python function that calculates the sum of all numbers in a list.
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((1,1,1,1,1)))

#Write a Python function to check whether a number is in a given range.
X = int(input("Enter minimum value of the range:"))
Y = int(input("Enter maximum value of the range:"))
n = int(input("Enter your number:"))
def test_range(n):
    if n in range(X,Y):
        print( "Number",n," %s is in the range",X,"to",Y%str(n))
    else :
        print("The number",n," is outside the given range of",X,"to",Y)
#input section
test_range(n)
