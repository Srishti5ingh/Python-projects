# this is a module for manipulating a URI

import re

def uri_manipulation(num):
    
    regex = r"(https?:\/\/(www\.)?)([^\/]+)\/([^\/]+)\/([^\/]+)\/(.*)"

    test_str = ("http://www.some_domain.com/some_other_slash/another_slash/\n"
    "https://www.some_domain.com/some_other_slash/another_slash/\n"
    "http://some_domain.co.uk/some_other_slash/another_slash/\n"
    "https://some_domain.co.uk/some_other_slash/another_slash/more_data_here")


    subst = '\\' + num

    # You can manually specify the number of replacements by changing the 4th argument
    result = re.sub(regex, subst, test_str, 0, re.MULTILINE)

    if result:
        print (result)