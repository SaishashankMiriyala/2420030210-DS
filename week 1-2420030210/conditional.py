"""fruits=["orange","apple","banana"]
for x in fruits:
    print(x)"""


"""for x in range(6):
    print(x)"""

"""for x in range(5,30,3):
    print(x)"""

"""even numbers
for x in range(2,100,2):
    print(x)"""

s = input("Enter a string: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
