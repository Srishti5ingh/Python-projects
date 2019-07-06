import mymodule2
print(" \n Enter any of the following numbers to get parts of the URI/URL : ")
n = input (" 1 for scheme \n 2 for sub-domain \n 3 for domain \n 4 for directory/path \n 5 for sub-directory/query \n 6 for page/fragment\n\n ")

#
try:
    if ( int(n) <=6 and int(n) > 0):
        mymodule2.uri_manipulation(n)
except ValueError:
    print("Invalid input")
