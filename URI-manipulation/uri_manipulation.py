# code using the uriModule
# the module contains 2 functions: uriManipulation & uriManipulation2

import uriModule

# choice variable is for choosing which function to use for manipulating the URL/URI
choice = -1
try:
    choice = int(input(" \n Enter 1 to parse given URL/URIs \n Enter 2 to enter your own URI/URL \n"))
except ValueError:
    print("Invalid input\n")
    exit()

if (choice == 1):
    print(" \n Enter any of the following numbers to get parts of the URI/URL : ")
    n = input(" 1 for scheme \n 2 for sub-domain \n 3 for domain \n 4 for directory/path \n 5 for sub-directory/query \n 6 for page/fragment\n\n ")

    try:
        if (type(n) != int):
            uriModule.uriManipulation(n)
    except TypeError:
        print("Your input must be a number\n")
 
elif(choice == 2):
    url = input("Enter a URL: ")
    print(" \n Enter any of the following numbers to get parts of the URI/URL : ")
    n = int(input(" 1 for scheme \n 2 for authority+domain \n 3 for directory/path \n 4 for sub-directory/query \n 5 page/fragment\n\n "))
    print(uriModule.uriManipulation2(url, n))

else:
    print("\nInvalid choice\n")

