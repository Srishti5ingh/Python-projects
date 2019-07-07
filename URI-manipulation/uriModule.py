# this is a module for parsing URL/URI

import re

# Function for parsing URLs, URLs are hard-coded 
def uriManipulation(num):

    if type(int(num)) not in [int]:
        raise TypeError(" Your input must be a number\n")

    if ( int(num) < 1 or int(num) > 6 ):
        raise ValueError(" Enter a number within the range\n")

    
    regex = r"(https?:\/\/(www\.)?)([^\/]+)\/([^\/]+)\/([^\/]+)\/(.*)"

    test_str = ("http://www.some_domain.com/some_other_slash/another_slash/\n"
    "https://www.some_domain.com/some_other_slash/another_slash/\n"
    "http://some_domain.co.uk/some_other_slash/another_slash/\n"
    "https://some_domain.co.uk/some_other_slash/another_slash/more_data_here")

    subst = '\\' + num

    # manually specify the number of replacements by changing the 4th argument
    result = re.sub(regex, subst, test_str, 0, re.MULTILINE)

    if result:
        print (result)


# Function for manipulating URIs as a user input

def uriManipulation2(url, num):

    if type(num) not in [int]:
        raise TypeError(" Your input must be a number\n")
    if (num < 1 or num > 5 ):
        raise ValueError(" Enter a number within the range 1 to 5\n")

    if (num == 1):
        search_group = 2
    elif (num == 2):
        search_group = 4
    elif (num == 3):
        search_group = 5
    elif (num == 4):
        search_group = 7
    elif (num == 5):
        search_group = 9

    # URIs syntax according to RFC[2396] docs
    #  $1 = http:
    #  $2 = http (scheme)
    #  $3 = //www.ics.uci.edu
    #  $4 = www.ics.uci.edu (domain)
    #  $5 = /pub/ietf/uri/ (path)
    #  $6 = <undefined>
    #  $7 = <undefined> (query)
    #  $8 = #Related
    #  $9 = Related (fragment)

    return re.fullmatch("^(([^:/?#]+):)?(\/\/([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?", url).group(search_group)
    